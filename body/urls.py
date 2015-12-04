from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import os
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'body.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
        
    url(r'^accounts/', include('userena.urls')),
    
    url(r'^accounts/signin/staff/show_staff/', 'staff.views.show_staff'),
    url(r'^accounts/signin/accounts/feedback/', 'accounts.views.feedback',name='feedback'),
 
    


    
    
)