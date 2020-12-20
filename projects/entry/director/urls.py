"""director URL Configuration"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.director, name="director"),
    path('dlogin', views.dlogin, name="dlogin"),
    path('home', views.home, name="home"),
    path('logout', views.logout, name="logout"),
    path('account', views.account, name="accont"),
    path('create_account', views.create_account, name="create_account"),
    path('checked', views.checked, name="checked"),
]
