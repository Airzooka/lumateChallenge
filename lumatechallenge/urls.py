"""URL Configuration for the entire Lumate Challenge project.

Serves the home page and two pages under /guestbook/.

"""
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'lumatechallenge.views.home', name='home'),
    url(r'^guestbook/', include('guestbook.urls', namespace='guestbook')),
    )