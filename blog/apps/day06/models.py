from django.db import models


class Department(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=30)
    
    def __str__(self):
        return "Department<d_id=%s, d_name=%s>" % (self.d_id, self.d_name)
    
    
class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=30)
    # 一对多，把表创建在多的一方
    dept = models.ForeignKey('Department', on_delete=models.CASCADE)
    # dept_id关联d_id
    
    def __str__(self):
        return "Student<s_id=%s, s_name=%s, dept_id=%s>" % (self.s_id, self.s_name, self.dept_id)


class Course(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=30)
    stu = models.ManyToManyField('Student')
    # 帮我们自动生成关系表:stu_id -> s_id


class Stu_detail(models.Model):
    student = models.OneToOneField('Student', on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.BooleanField(default=True)
    city = models.CharField(max_length=30, null=True)
