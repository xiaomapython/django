from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('index/', views.index, name="blog_index"),
    path('add/', views.add, name="blog_add"),
    path('detail/<int:id>', views.detail, name="blog_detail"),
    path('list/', views.list, name="blog_list"),
    path('edit/<int:id>', views.edit, name="blog_edit"),
    path('delete/<int:id>', views.delete, name="blog_delete"),

]
