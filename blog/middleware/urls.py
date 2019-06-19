from django.urls import path, re_path

from . import views

urlpatterns = [
    path("exception/", views.test_exception)
]
