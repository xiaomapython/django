from django.urls import path

from . import views


urlpatterns = [
    path('post/', views.post_test),
    path('get/', views.get_req),
    path('get_name/', views.get_test),
    path('set_ck/', views.set_ck),
    path('get_ck/', views.get_ck),
    path('del_ck/', views.delete_ck),

]
