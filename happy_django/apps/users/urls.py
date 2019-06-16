from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # path('login/', views.login, name="users_login"),
    path('login/', views.LoginView.as_view(), name="users_login"),
    # path('register/', views.register, name="users_register"),
    path('register/', views.RegisterView.as_view(), name='users_register'),
    path('logout/', views.LogoutView.as_view(), name='users_logout'),
]
