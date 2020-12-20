from django.contrib import admin
from . models import gaurds
from . models import guest_entries

# Register your models here.
admin.site.register(gaurds)
admin.site.register(guest_entries)