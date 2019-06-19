from django.urls import path

from . import views

app_name = "upload"

urlpatterns = [
    path('upload/', views.upload, name="file_upload"),

]
