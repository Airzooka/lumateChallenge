from django.shortcuts import render, redirect
from django.template import loader
from guestbook.models import Entry

def index(request):
    context = {
        'entries_list': Entry.objects.order_by('-datetime')
        }
    return render(request, 'guestbook/index.html', context)

def write(request):
    if request.method == 'POST':
        try:
            new_entry = Entry(
                ip=request.META['REMOTE_ADDR'],
                nameFirst=request.POST['namefirst'],
                nameLast=request.Post['namelast'],
                comment=request.POST['comment']
                )
            new_entry.full_clean()
            new_entry.save(force_insert=True)
        except ValidationError as e:
            guestbook_error = '<br />'.join(e.messages)
        else:
            return redirect('index.html')
    context = {
        'guestbook_error': guestbook_error
        }
    return render(request, 'guestbook/write.html', context)