from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User, Permission, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required

from blog.forms import LoginForm, RegisterForm
from .models import Blog
# Create your views here.


@login_required
def index(request):
    return render(request, "blog/demo_index.html")


# app名字.codename
@permission_required("blog.add_blog", login_url="/blog/index/")
def add(request):
    if request.method == "GET":
        return render(request, "blog/demo_add.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Blog.objects.create(title=title, content=content)
        
        return redirect(reverse("blog:blog_list"))


@login_required
def detail(request, id):
    blog = Blog.objects.filter(id=id)[0]
    return render(request, "blog/demo_detail.html", locals())


@login_required
def list(request):
    blog = Blog.objects.all()
    return render(request, "blog/demo_list.html", locals())


@login_required
def edit(request, id):
    if request.method == "GET":
        blog = Blog.objects.filter(id=id)[0]
        return render(request, "blog/demo_edit.html", locals())
    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        # 查出相关数据
        blog = Blog.objects.filter(id=id)
        # 更改数据
        blog.update(title=title, content=content)
        return redirect(reverse("blog:blog_list"))


@login_required
def delete(request, id):
    blog = Blog.objects.filter(id=id)[0]
    if blog:
        blog.delete()
        return redirect(reverse("blog:blog_list"))
    else:
        return HttpResponse("文章不存在！")


def register_test(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "blog/demo_register.html", context={"form": form})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            password_repeat = form.cleaned_data.get("password_repeat")
            email = form.cleaned_data.get("email")
            # if password == password_repeat:
            #     password = make_password(password)  # 对密码进行加密
            #     UserModel.objects.get_or_create(username=username, password=password, email=email)
            #     return redirect(reverse("form:login_form"))
            
            if password == password_repeat:
                # 修改用户表，把用户存储到 auth_user 中
                User.objects.create_user(username=username, password=password, email=email)
                return redirect(reverse("blog:blog_login"))
            else:
                return render(request, "blog/demo_register.html",
                              context={"form": form, "error": "两次输入密码不一致，请重新输入"})
        else:
            # return redirect(reverse("form:reg_form"))
            return render(request, "blog/demo_register.html", context={"form": form, "error": form.errors})


def login_test(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "blog/demo_login.html", context={"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            # user = UserModel.objects.filter(username=username)
            # 认证账号与密码
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                # if check_password(password, user[0].password):
                #     request.session["username"] = username  # 保存状态
                #     return render(request, "form/home.html", context={"name": username})
                # else:
                #     return render(
                #         request, "form/login.html",
                #         context={"form": form, "error": "请输入正确的密码"}
                #
                login(request, user)  # 保存状态
                
                next_url = request.GET.get("next")
                if next_url:
                    return redirect(next_url)
                
                return redirect(reverse("blog:blog_index"))
            else:
                return render(
                    request, "blog/demo_login.html",
                    context={"form": form, "error": form.errors}
                )
        else:
            return render(
                request, "blog/demo_login.html",
                context={"form": form, "error": "请确认账户或密码"}
            )


def logout_test(request):
    logout(request)
    return redirect(reverse("blog:blog_login"))


def auth_test(request):
    user = User.objects.filter(username="xiaohong").first()
    # user.set_password("mjc123")
    # 此处必须要使用save保存，不然密码修改不成功
    # user.save()
    
    # 为某个成员添加权限
    add_blog = Permission.objects.filter(codename="add_blog").first()
    # print(add_blog)
    # user.user_permissions.add(add_blog)
    
    # 组操作
    # 创建组
    Group.objects.get_or_create(name="add_blog_group")
    # 给组添加权限
    g = Group.objects.filter(name="add_blog_group").first()
    # g.permissions.add(add_blog)
    
    budong = User.objects.filter(username="budong").first()
    # 把成员添加到组里面
    g.user_set.add(budong)
    return HttpResponse("修改成功")



