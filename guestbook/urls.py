"""URL Configuration for the website guestbook.

Serves one page for the index, which lists guestbook entries, and another for
adding an entry.

In the Lumate Challenge project, URLs here live in the "guestbook" namespace
and are relative to /guestbook/.

"""
from django.conf.urls import patterns, url
from guestbook import views

urlpatterns = patterns('',
    url(r'^$', 'guestbook.views.index', name='index'),
    url(r'^write/', 'guestbook.views.write', name='write'),
    )