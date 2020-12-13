"""director URL Configuration"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.director, name="director"),
    path('dlogin', views.dlogin, name="dlogin"),
    path('home', views.home, name="home"),
]
