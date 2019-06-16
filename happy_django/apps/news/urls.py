from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name="news_index"),
    path('news/', views.NewsListView.as_view(), name="news_list"),
    path('news/banners/', views.NewsBanner.as_view(), name='news_banner'),
    path('news/detail/<int:news_id>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('news/<int:news_id>/comments/', views.NewsCommentView.as_view(), name='news_comment'),
    
    path('search/', views.SearchView(), name="news_search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
