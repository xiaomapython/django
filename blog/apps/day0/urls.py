"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from . import views
urlpatterns = [
    path('hello/', views.hello),
    path('hello_mjc/', views.hello_mjc),
    path('hello_everyone/<name>/', views.hello_everyone),
    # path('hello_every/<name>/<age>/', views.hello_every),
    path('hello_every/<name>/<int:age>/', views.hello_every),
    path('hello_kwargs/', views.hello_kwargs, {'name': 'mjc'}),  # 常用可以在后面增加开关
    
]
