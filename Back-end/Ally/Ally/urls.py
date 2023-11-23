"""Ally URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from main.forum import *
from main.root import api_root
from main.hackathon import *

urlpatterns = [
    path("", api_root),
    path('admin/', admin.site.urls),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('comment_post/', AddCommentView.as_view(), name='comment_post'),
    path('react_post/', AddReactionView.as_view(), name='react_post'),
    path('posts/<int:forumID>/', ListPostView.as_view(), name='post_list'),
    path('create_hackathon/',createHackathon,name='create_hackathon'),
    path('get_hackathon/',getHackathon,name='get_hackathon'),
    path('register_hackathon/',registerHackathon,name='register_hackathon'),
    path('registered_hackathon/',getHackReg,name='registered_hackathon'),
]
