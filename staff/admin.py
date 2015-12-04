#-*- coding:utf-8 -*-
from django.contrib import admin
from accounts.models import Staff
from django.contrib.auth.models import User

# Register your models here.


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'available_time', 'statu','staffstatu',)
admin.site.register(Staff,StaffAdmin)