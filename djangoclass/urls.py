from django.conf.urls import patterns, include, url
from timer.views import hello, current_datetime, hours_ahead

urlpatterns = patterns('',
    # Examples:
    url(r'^$', controllers.index),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
