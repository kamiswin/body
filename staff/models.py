#-*- coding:utf-8 -*-
from django.contrib.auth.models import User  
from django.utils.translation import ugettext as _  
 
from django.db import models
# Create your models here.
staffstatus = (
    (u'上班', u'上班'),
    (u'休息', u'休息'),
    )       

status = (
    (u'排钟', u'排钟'),
    (u'上钟', u'上钟'),
    (u'休息', u'休息'),
    )  
    


class Staff(models.Model):

    name = models.CharField(u'技师姓名',max_length=20,null=True)
    available_time = models.TimeField(u'可以预约时间',null=True)
    statu = models.CharField(u'技师状态',max_length=20,choices=status,null=True)
    staffstatu = models.CharField(u'技师班况',choices=staffstatus,max_length=20,null=True)
    
    
    class Meta:
        db_table = 'staff'
        verbose_name='技师在岗'
        verbose_name_plural='技师在岗'