from django.shortcuts import render
from django.template import loader
from guestbook.models import Entry

def index(request):
    context = {
        'entries_list': Entry.objects.order_by('-datetime')
        }
    return render(request, 'guestbook/index.html', context)

def write(request):
    Entry.objects.create(
        nameFirst=request.POST['nameFirst']
        nameLast=request.post['nameLast']
    )
    context = {
        ''
        }
    return render(request, 'guestbook/write.html', context)