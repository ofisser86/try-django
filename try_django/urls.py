"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from blog.views import blog_post_create_view
from .views import (
        home_page,
        about_page,
        contact_page,
        render_txt
)

urlpatterns = [
    path('', home_page, name='home'),

    path('blog/', include('blog.urls')),
    path('blog-new/', blog_post_create_view, name='new-post'),

    # re_path(r'^blog/(?P<post_id>\d+)/$', blog_post_detail_page, name='blog'),
    path('txt', render_txt),
    path('contact/', contact_page, name='contact'),
    path('about/', about_page),
    path('admin/', admin.site.urls),
]
