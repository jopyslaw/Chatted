"""Chatted URL Configuration

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
from django.conf.urls import include
from website.views import *
from chat.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    path('app_dsc', app_dsc, name="app_dsc"),
    path('contact', contact, name="contact"),
    path('about', about, name="about"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('login/logged_user', check_login_data, name="check_login_data"),
    path('logout', logout, name="logout"),
    path('register/register_user', register_user, name="register_user"),
    path('edit_account', edit_account, name="edit_account"),
    path('user_page', user_page, name="user_page"),
    path('no_log_after', no_log_after, name="no_log_after"),
    path('chat/', include('chat.urls')),
]
