from django.urls import path
from . import views
from .views import HomeView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CategoryCreateView , CategoryView, LikeView

urlpatterns=[
    path(r'', HomeView.as_view(), name='home'),
    path(r'post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path(r'post/new', PostCreateView.as_view(), name='new_post'),
    path(r'post/edit/<int:pk>', PostUpdateView.as_view(), name='update_post'),
    path(r'post/delete/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
    path(r'category/new', CategoryCreateView.as_view(), name='new_category'),
    path(r'category/<str:cats>', CategoryView, name='category'),
    path(r'like/<int:pk>', LikeView, name='like_post'),
]