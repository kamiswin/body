#-*- coding:utf-8 -*-
from django.contrib import admin
from accounts.models import Feedback,Staffachive,Profit,Room
from django.contrib.auth.models import User



class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('text',)
admin.site.register(Feedback,FeedbackAdmin)

class StaffachiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'room', 'service_time','proname',)
admin.site.register(Staffachive,StaffachiveAdmin)

class ProfitAdmin(admin.ModelAdmin):
    list_display = ('money', 'waytopay',)
admin.site.register(Profit,ProfitAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room', 'roomstatu',)
admin.site.register(Room,RoomAdmin)