import json
import logging
import string

import random
from django.views import View
from django_redis import get_redis_connection
from django.http import HttpResponse

from utils.captcha.captcha import captcha
# 安装图片验证码所需要的 Pillow 模块
# pip install Pillow
from . import constants
from users.models import Users
from utils.json_fun import to_json_data
from utils.res_code import Code, error_map

from . import forms
from utils.yuntongxun.sms import CCP


'''
    # 1、创建视图
    # 2、从前端获取参数
    # 3、校验参数
    # 4、生成图片验证码图片以及图片验证码文本
    # 5、保存图片验证码文本到redis
    # 6、返回图片验证码图片给前端
'''

# 导入日志器
logger = logging.getLogger('django')


class ImageCode(View):
    """
    define image verification view
    # /image_codes/<uuid:image_code_id>/
    """

    def get(self, request, image_code_id):
        text, image = captcha.generate_captcha()

        # 确保settings.py文件中有配置redis CACHE
        # Redis原生指令参考 http://redisdoc.com/index.html
        # Redis python客户端 方法参考 http://redis-py.readthedocs.io/en/latest/#indices-and-tables
        con_redis = get_redis_connection(alias='verify_codes')
        img_key = "img_{}".format(image_code_id).encode('utf-8')
        # 将图片验证码的key和验证码文本保存到redis中，并设置过期时间
        con_redis.setex(img_key, constants.IMAGE_CODE_REDIS_EXPIRES, text)
        logger.info("Image code: {}".format(text))

        return HttpResponse(content=image, content_type="images/jpg")


class CheckUsernameView(View):
    """
    Check whether the user exists
    GET usernames/(?P<username>\w{5,20})/
    """
    def get(self, request, username):

        # count = 1 if User.objects.get(username=username) else 0
        data = {
            'username': username,
            'count': Users.objects.filter(username=username).count()
        }
        return to_json_data(data=data)


class CheckMobileView(View):
    """
    Check whether the mobile exists
    GET mobiles/(?P<mobile>1[3-9]\d{9})/
    """
    def get(self, request, mobile):

        data = {
            'mobile': mobile,
            'count': Users.objects.filter(mobile=mobile).count()
        }
        return to_json_data(data=data)


# 导入日志器
logger = logging.getLogger('django')


class SmsCodesView(View):
    """
    send mobile sms code
    POST /sms_codes/
    """
    def post(self, request):
        # 1、
        json_data = request.body
        print(json_data)
        if not json_data:
            return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])
        # 将json转化为dict
        dict_data = json.loads(json_data.decode('utf8'))
        # 2、
        form = forms.CheckImgCodeForm(data=dict_data)
        if form.is_valid():
            # 获取手机号
            mobile = form.cleaned_data.get('mobile')
            # 3、
            # 创建短信验证码内容
            sms_num = ''.join([random.choice(string.digits) for _ in range(constants.SMS_CODE_NUMS)])

            # 将短信验证码保存到数据库
            # 确保settings.py文件中有配置redis CACHE
            # Redis原生指令参考 http://redisdoc.com/index.html
            # Redis python客户端 方法参考 http://redis-py.readthedocs.io/en/latest/#indices-and-tables
            # 4、
            redis_conn = get_redis_connection(alias='verify_codes')
            pl = redis_conn.pipeline()

            # 创建一个在60s以内是否有发送短信记录的标记
            sms_flag_fmt = "sms_flag_{}".format(mobile)
            # 创建保存短信验证码的标记key
            sms_text_fmt = "sms_{}".format(mobile)

            # 此处设置为True会出现bug
            try:
                pl.setex(sms_flag_fmt.encode('utf8'), constants.SEND_SMS_CODE_INTERVAL, 1)
                pl.setex(sms_text_fmt.encode('utf8'), constants.SMS_CODE_REDIS_EXPIRES, sms_num)
                # 让管道通知redis执行命令
                pl.execute()
            except Exception as e:
                logger.debug("redis 执行出现异常：{}".format(e))
                return to_json_data(errno=Code.UNKOWNERR, errmsg=error_map[Code.UNKOWNERR])

            logger.info("Sms code: {}".format(sms_num))

            # 发送短语验证码
            # try:
            #     result = CCP().send_template_sms(mobile,
            #                                      [sms_num, constants.SMS_CODE_REDIS_EXPIRES],
            #                                      constants.SMS_CODE_TEMP_ID)
            #     print("验证码发送成功")
            # except Exception as e:
            #     logger.error("发送验证码短信[异常][ mobile: %s, message: %s ]" % (mobile, e))
            #     return to_json_data(errno=Code.SMSERROR, errmsg=error_map[Code.SMSERROR])
            # else:
            #     if result == 0:
            #         logger.info("发送验证码短信[正常][ mobile: %s sms_code: %s]" % (mobile, sms_num))
            #         return to_json_data(errno=Code.OK, errmsg="短信验证码发送成功")
            #     else:
            #         logger.warning("发送验证码短信[失败][ mobile: %s ]" % mobile)
            #         return to_json_data(errno=Code.SMSFAIL, errmsg=error_map[Code.SMSFAIL])
            return to_json_data(errmsg="><发送验证码成功><")
        else:
            # 定义一个错误信息列表
            err_msg_list = []
            for item in form.errors.get_json_data().values():
                err_msg_list.append(item[0].get('message'))
                # print(item[0].get('message'))   # for test
            err_msg_str = '/'.join(err_msg_list)  # 拼接错误信息为一个字符串

            return to_json_data(errno=Code.PARAMERR, errmsg=err_msg_str)
