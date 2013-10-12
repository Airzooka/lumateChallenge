from django.shortcuts import render
from guestbook.models import Entry

def index(request):
    context = {
        'EntriesList': Entry.objects.order_by('-datetime')
        }
    return render(request, 'guestbook/index.html', context)

def write(request):
    return HttpResponse("")