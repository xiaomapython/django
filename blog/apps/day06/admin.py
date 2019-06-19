from django.contrib import admin

from .models import Department, Student, Stu_detail, Course

"""
Django提供了admin.ModelAdmin类
通过定义ModelAdmin的子类，来定义模型在Admin界面的显示方式
1、列表页属性(通俗的讲就是操作字段)：
    list_display   显示字段，可以点击字段进行排序
    list_filter    过滤字段，过滤框会出现在右侧
    search_fields  搜索字段，搜索框会出现在上侧
    list_per_page  分页，分页框会出现在下侧
2、添加，修改页属性(通俗的讲就是操作字段)：
    fields          属性的先后顺序
    fieldsets       属性分组
    注意：上面两个属性，二者选一
    
"""


class DeptAdmin(admin.ModelAdmin):
    list_display = ['d_id', 'd_name']
    list_display_links = ['d_name']


class Stu_detailAdmin(admin.ModelAdmin):
    # fields = ['student', 'age', 'city']
    fieldsets = [
        ("一", {"fields": ["student"]}),
        ("二", {"fields": ["age", "city"]}),
    ]


class StudentAdmin(admin.ModelAdmin):
    list_per_page = 3  # 设置每页显示的数量
    

admin.site.register(Department, DeptAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Stu_detail, Stu_detailAdmin)
admin.site.register(Course)
