"""entry URL Configuration"""
from django.contrib import admin
from django.urls import path,include
from . import views
admin.site.site_header="Entry & Exit System"
admin.site.site_title="Entry & Exit System"
admin.site.index_title="Entry & Exit System"

urlpatterns = [
    path('', views.index, name="index"),
    path('director/', include('director.urls')),
    path('gaurd/', include('gaurd.urls')),
    path('admin/', admin.site.urls),
]
