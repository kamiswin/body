# coding:utf-8
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import models
from django.contrib.auth.models import User

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.db import models
from django.shortcuts import render_to_response,HttpResponse,render
from django.core.mail import send_mail


from staff.models import Staff


    
def show_staff(req):
    staffs = Staff.objects.all()
    return render_to_response('staff/show_staff.html',{'staffs':staffs})