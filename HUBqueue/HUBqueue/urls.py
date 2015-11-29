from django.conf.urls import patterns, include, url
from django.contrib import admin

from HUBqueue.main import index
from Register.RegisterUnit import handler as regHandler
from Schedule.ScheduleUnit import handler as schHandler

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HUBqueue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', regHandler),
    url(r'^schedule/$', schHandler),
    url(r'^$', index),
)
