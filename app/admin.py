from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Image)
class imageModeladmin(admin.ModelAdmin):
    list_display = ('id','date','image')