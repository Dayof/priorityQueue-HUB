from django.conf.urls import patterns, include, url
from django.contrib import admin

from HUBqueue.main import UiMain
from Register.RegisterUnit import UiRegister
from Schedule.ScheduleUnit import UiSchedule

UiMain = UiMain()
UiRegister = UiRegister()
UiSchedule = UiSchedule()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HUBqueue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', UiRegister.run),
    url(r'^register/(?P<model>\w{3,25})/$', UiRegister.run),
    url(r'^schedule/$', UiSchedule.run),
    url(r'^$', UiMain.run),
)
