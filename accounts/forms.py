#!/usr/bin/python
#coding:utf-8
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django import forms
import re


class FeedbackForm(forms.Form):

    text = forms.CharField(widget = forms.Textarea)



    
       