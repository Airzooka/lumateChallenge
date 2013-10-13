from django.conf.urls import patterns, url

from guestbook import views

urlpatterns = patterns('',
    url(r'^$', 'guestbook.views.index', name='index'),
    url(r'^write/', 'guestbook.views.write', name='write'),
    )