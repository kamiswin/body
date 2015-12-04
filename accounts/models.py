#-*- coding:utf-8 -*-
from django.contrib.auth.models import User  
from django.utils.translation import ugettext as _  
from userena.models import UserenaBaseProfile  
from django.db import models

class Feedback(models.Model):

    text = models.CharField(u'意见建议',max_length=255,null=True)
    
    
    class Meta:
        db_table = 'Feedback'
        verbose_name='意见建议'
        verbose_name_plural='意见建议'


  
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
        
rooms = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    )          
pronames = (
    (u'全身', u'全身'),
    (u'半身', u'半身'),
    (u'足疗', u'足疗'),
    (u'全身加脚',u'全身加脚'),
    )
class Staffachive(models.Model):
    name = models.CharField(u'技师姓名',max_length=20,null=True)
    room = models.CharField(u'房间号码',max_length=20,choices=rooms,null=True)
    service_time = models.TimeField(u'服务日期时间',null=True)
    proname = models.CharField(u'项目',max_length=20,choices=pronames,null=True)

    class Meta:
        db_table = 'staffachive'
        verbose_name='技师业绩'
        verbose_name_plural='技师业绩'

waytopays = (
    (u'现金', u'现金'),
    (u'银行卡', u'银行卡'),
    )  
class Profit(models.Model):
    money = models.CharField(u'金额',max_length=20,null=True)
    waytopay = models.CharField(u'付款方式',max_length=20,choices=waytopays,null=True)
    

    class Meta:
        db_table = 'profit'
        verbose_name='营业数据'
        verbose_name_plural='营业数据'
        
        
rooms = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    )    
    
roomstatus = (
    (u'闲置',u'闲置'),
    (u'使用',u'使用'),
    )          
class Room(models.Model):
    room = models.CharField(u'房间号码',max_length=20,choices=rooms,null=True)
    roomstatu = models.CharField(u'房间状态',max_length=20,choices=roomstatus,null=True)
    

    class Meta:
        db_table = 'Room'
        verbose_name='房间'
        verbose_name_plural='房间'

pickstaffs = (
    ('JADE', 'Jade'),
    ('LILI', 'Lili'),
    ('ISA', 'Isa'),
    )   
   
dates = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31'),
)
    
times = (
    ('10:00', '10:00'),
    ('10:15', '10:15'),
    ('10:30', '10:30'), 
    ('10:45', '10:45'), 
    ('11:00', '11:00'),
    ('11:15', '11:15'),
    ('11:30', '11:30'), 
    ('11:45', '11:45'), 
    ('12:00', '12:00'),
    ('12:15', '12:15'),
    ('12:30', '12:30'), 
    ('12:45', '12:45'), 
    ('13:00', '13:00'),
    ('13:15', '13:15'),
    ('13:30', '13:30'), 
    ('13:45', '13:45'), 
    ('14:00', '14:00'),
    ('14:15', '14:15'),
    ('14:30', '14:30'), 
    ('14:45', '14:45'), 
    ('15:00', '15:00'),
    ('15:15', '15:15'),
    ('15:30', '15:30'), 
    ('15:45', '15:45'), 
    ('16:00', '16:00'),
    ('16:15', '16:15'),
    ('16:30', '16:30'), 
    ('16:45', '16:45'), 
    ('17:00', '17:00'),
    ('17:15', '17:15'),
    ('17:30', '17:30'), 
    ('17:45', '17:45'), 
    ('18:00', '18:00'),
    ('18:15', '18:15'),
    ('18:30', '18:30'), 
    ('18:45', '18:45'), 
    ('19:00', '19:00'),
    ('19:15', '19:15'),
    ('19:30', '19:30'), 
    ('19:45', '19:45'), 
    ('20:00', '20:00'),
    ('20:15', '20:15'),
    ('20:30', '20:30'), 
    ('20:45', '20:45'),  
    )
    
palces = (
    ('home service', 'home service'),
    ('store service', 'store service'),
    )
    
periods = (
    ('30mins 35dollors', '30mins 35dollors'),
    ('45mins 50dollors', '45mins 50dollors'),
    ('60mins 60dollors', '60mins 60dollors'),
    ('75mins 75dollors', '75mins 75dollors'),
    ('90mins 90dollors', '90mins 90dollors'),
    ('120mins 120dollors', '120mins 120dollors'),
    ('over 2 hours ', 'over 2 hours '),
    )
class MyProfile(UserenaBaseProfile):  
    user = models.OneToOneField(User,unique=True,  
                        verbose_name=_('user'),related_name='my_profile')  
   
                        
                        
    phone = models.CharField(u'Phone',max_length=10,null=True,blank=True)
    vip_card_expire_date = models.DateField(u'贵宾卡到期',max_length=30,null=True)
    blance = models.CharField(u'账号余额',max_length=30,null=True)
    pickstaff = models.CharField(u'Select masseur',max_length=25,choices=pickstaffs,null=True)
    date = models.CharField(u'Select date',max_length=99,choices=dates,null=True)
    time = models.CharField(u'Select time',max_length=99,choices=times,null=True)
    period = models.CharField(u'How long would you like.(Minimum 60 mins for home service)',max_length=99,choices=periods,null=True)
    home_or_store = models.CharField(u'Select the place you want ',max_length=99,choices=palces,null=True)
    address = models.CharField(u'Enter your address or leave it in blank if you come to us',max_length=180,null=True,blank=True)
    
    class Meta:
        db_table = 'accounts_myprofile'
        verbose_name='客人信息'
        verbose_name_plural='客人信息'
    
