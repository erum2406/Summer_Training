"""gaurd URL Configuration"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gaurd, name="gaurd"),
    path('glogin', views.glogin, name="glogin"),
]
