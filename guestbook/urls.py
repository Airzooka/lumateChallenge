from django.conf.urls import patterns, url

from guestbook import views

urlpatterns = patterns('',
    url(r'^$', 'views.index', name='index'),
    url(r'^write/', 'views.write', name='write'),
    )