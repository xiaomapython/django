from django.http import HttpResponse

from .models import Department, Stu_detail, Student, Course


def dept(request):
    # Department.objects.get_or_create(d_name="软件学院")
    # Department.objects.get_or_create(d_name="机械学院")
    # Department.objects.get_or_create(d_name="土木学院")
    # Department.objects.get_or_create(d_name="社会学院")
    # Student.objects.get_or_create(s_name="朱世勇", dept_id=1)
    # Student.objects.get_or_create(s_name="张学友", dept_id=1)
    # Student.objects.get_or_create(s_name="王菲", dept_id=1)
    # Student.objects.get_or_create(s_name="刘德华", dept_id=2)
    # Student.objects.get_or_create(s_name="霍建华", dept_id=2)
    # Student.objects.get_or_create(s_name="刘亦菲", dept_id=2)
    # Student.objects.get_or_create(s_name="黎明", dept_id=3)
    # Student.objects.get_or_create(s_name="郭富城", dept_id=3)
    # Student.objects.get_or_create(s_name="唐僧", dept_id=4)
    # Student.objects.get_or_create(s_name="孙悟空", dept_id=4)
    print("*****************"*3, "一对多关系查询", "*****************"*3)
    s1 = Student.objects.get(s_id=1)
    print(s1)
    print(s1.s_name)
    print(s1.dept_id)
    print(s1.dept)  # 返回的是Department的实例对象
    print('-----------------------------'*4)
    # 进行反查
    d1 = Department.objects.get(d_id=1)
    print(d1)
    print(d1.d_name)
    print(d1.student_set)  # 反向查询的时候提供的一种管理器，day06.Student.None
    print(d1.student_set.all())  # all拿到所有的数据：<QuerySet [<Student: Student<s_id=1, s_name=朱世勇, dept_id=1>>, <Student: Student<s_id=2, s_name=张学友, dept_id=1>>]>
    
    d2 = Department.objects.get(d_id=2)
    
    # add() 修改 数据已经存在 一对多，多对多
    # 把朱世勇同学从软件学院转到机械学院
    # d2.student_set.add(s1)
    # create 新建数据 一对多，多对多
    # 机械学院中增加张靓颖同学
    d2.student_set.get_or_create(s_name="张靓颖")
    
    return HttpResponse('xxxxxxx')
