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

from accounts.forms import FeedbackForm
from accounts.models import Feedback


def feedback(request):

    if request.method == 'POST':
        fm = FeedbackForm(request.POST)
        if fm.is_valid():
            text = fm.cleaned_data['text']
            
            feedback = Feedback()
            feedback.text = text
            
            feedback.save()
            
 
            return render_to_response('accounts/feedbackwarn.html',{'feedbackwarn':feedbackwarn,},
                    context_instance=RequestContext(request))
        
    else:
        fm = FeedbackForm()

    return render_to_response('accounts/feedback.html',{'fm':fm,},
                    context_instance=RequestContext(request)) 

 
def index (req):
    return render_to_response("index.html",{'index':index})
        
def right (req):
    return render_to_response("right.html",{'right':right})
        
def offers (req):
    return render_to_response("offers.html",{'offers':offers})
        
def contact (req):
    return render_to_response("contact.html",{'contact':contact})
        
      
def info (req):
    return render_to_response("info.html",{'info':info})
        
def pics (req):
    return render_to_response("pics.html",{'pics':pics})
        

def feedbackwarn (req):
    return render_to_response("feedbackwarn.html",{'feedbackwarn':feedbackwarn})
        
       
      
       






