"""Views to use on the website's guestbook section.

This module contains a function for the guestbook index (listing) view and the
writing view, respectively named index and write.
"""
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template import loader
from guestbook.models import Entry


def index(request):
    """View to use as the guestbook index page.
    
    Presents a list of all guestbook entries. Ideally the template will
    provide a link to writing one, using the write view.
    
    A Django HTTP Request object must be passed. An HTTP Response is returned.
    """
    context = {'entries_list': Entry.objects.order_by('-datetime')}
    return render(request, 'guestbook/index.html', context)

    
def write(request):
    """View to use as the guestbook writing page.
    
    Presents a form to write an entry into the guestbook. Upon submitting, the
    form values are validated and saved to the database, representing a
    digital signature.
    
    If form validation fails, the form is shown again along with an error
    message.
    
    A Django HTTP Request object must be passed. An HTTP Response is returned.
    """
    guestbook_error = None
    if request.method == 'POST':
        try:
            new_entry = Entry(
                ip=request.META['REMOTE_ADDR'],
                namefirst=request.POST['namefirst'],
                namelast=request.POST['namelast'],
                comment=request.POST['comment']
                )
            new_entry.full_clean()
            new_entry.save(force_insert=True)
        except ValidationError as e:
            guestbook_error = '<br /><br />'.join(e.messages)
        else:
            return redirect(reverse('guestbook:index'))
    context = {'guestbook_error': guestbook_error}
    return render(request, 'guestbook/write.html', context)