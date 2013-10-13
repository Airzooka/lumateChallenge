from django.shortcuts import render, redirect
from django.template import loader

def home(request):
    return render(request, 'home.html')