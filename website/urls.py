"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls.conf import include
from .customviews import redirect_view
from django.contrib.auth import views as auth_views
from music import MyAPIViews
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('SongsView', MyAPIViews.SongsView.as_view(), name='API'),                      
    re_path(r'^SongsView/$', MyAPIViews.SongsView.as_view()),
    path('', redirect_view)
]

urlpatterns = format_suffix_patterns(urlpatterns)