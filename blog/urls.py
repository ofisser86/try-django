from django.urls import path, re_path
from .views import (
    blog_post_detail_view,
    blog_post_list_view,
    blog_post_update_view,
    blog_post_delete_view,
)

urlpatterns = [
    path('', blog_post_list_view, name='blog'),
    path('<str:slug>/', blog_post_detail_view, name='blog-detail'),
    path('<str:slug>/edit/', blog_post_update_view, name='update-post'),
    path('<str:slug>/delete/', blog_post_delete_view, name='delete-post'),
]
