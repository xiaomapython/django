from django.urls import path, re_path

from . import views

app_name = "doc"

urlpatterns = [
    path('docs/', views.doc_index, name='doc_index'),
    path('docs/<int:doc_id>/', views.DocDownload.as_view(), name='doc_download'),
]






