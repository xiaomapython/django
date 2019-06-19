import os
from django.http import HttpResponse
from django.shortcuts import render

from blog_demo.settings import MEDIA_ROOT

# Create your views here.


def upload(request):
    if request.method == "GET":
        return render(request, "upload/upload_file.html")
    elif request.method == "POST":
        # print(request.FILES.get("file"))
        f = request.FILES.get("file")
        print(f.name)
        f_name = os.path.join(MEDIA_ROOT, f.name)
        
        with open(f_name, "wb") as ff:
            for c in f.chunks():
                ff.write(c)
        return HttpResponse("xxx")
