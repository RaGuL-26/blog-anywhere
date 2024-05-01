"""
URL configuration for myblogapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from posts import views as PostViews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',PostViews.home_page,name='home_page'),
    path('signup',PostViews.signup_page,name='signup_page'),
    path('signin',PostViews.signin_page,name='signin_page'),
    path('postspage',PostViews.posts_page,name='posts_page'),
    path('logoutpage',PostViews.logout_page,name='logout_page'),
    path('viewpost',PostViews.view_post_page,name='viewpost'),
    path('updatepost/<int:id>',PostViews.update_post,name='update_post'),
    path('addpost',PostViews.add_post,name='add_post'),
    path('aboutpage',PostViews.about_page,name='about_page'),
    path('<slug:slug>',PostViews.using_slug,name='using_slug'),
    path('deletepost/<int:id>',PostViews.delete_post,name='delete_post'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)