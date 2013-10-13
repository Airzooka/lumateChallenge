from django.shortcuts import render, redirect
from django.template import loader
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from guestbook.models import Entry

def index(request):
    context = {
        'entries_list': Entry.objects.order_by('-datetime')
        }
    return render(request, 'guestbook/index.html', context)

def write(request):
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
    context = {
        'guestbook_error': guestbook_error
        }
    return render(request, 'guestbook/write.html', context)