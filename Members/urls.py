from re import template
from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, FollowerView, ShowProfilePageView, EditProfilePageView
from BlogApp.tools import stats
from django.contrib.auth import views as auth_views
from . import views



urlpatterns=[
    path(r'register/', UserRegisterView.as_view(), name='register'),
    path(r'edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path(r'password/', PasswordsChangeView.as_view(), name='password'),
    path(r'password_success/', views.password_success, name='password_success'),
    path(r'follow/<int:pk>', FollowerView, name='follow'),
    path(r'<int:pk>/stats/', stats, name='stats'),
    path(r'<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path(r'<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
]