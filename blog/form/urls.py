from django.urls import path, re_path

from . import views

app_name = "form"

urlpatterns = [
    path("reg/", views.register_test, name="reg_form"),
    path("login/", views.login_test, name="login_form"),
]