from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from .models import Blog
# Create your views here.


def index(request):
    return render(request, "blog/demo_index.html")


def add(request):
    if request.method == "GET":
        return render(request, "blog/demo_add.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Blog.objects.create(title=title, content=content)
        
        return redirect(reverse("blog:blog_list"))


def detail(request, id):
    blog = Blog.objects.filter(id=id)[0]
    return render(request, "blog/demo_detail.html", locals())


def list(request):
    blog = Blog.objects.all()
    return render(request, "blog/demo_list.html", locals())


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


def delete(request, id):
    blog = Blog.objects.filter(id=id)[0]
    if blog:
        blog.delete()
        return redirect(reverse("blog:blog_list"))
    else:
        return HttpResponse("文章不存在！")

