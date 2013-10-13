"""Views to use on miscellaneous Lumate Challenge project pages.

This module contains a function for the index page named home.

"""
from django.shortcuts import render, redirect
from django.template import loader


def home(request):
    """View to use on the home page. Simply sends the home template."""
    return render(request, 'home.html')