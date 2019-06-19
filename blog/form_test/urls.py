from django.urls import path, re_path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/", views.login_test, name="login"),
    path("logout/", views.logout_test, name="logout"),
]
