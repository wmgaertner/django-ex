import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, request
from .forms import *

from . import database
from .models import PageView

# Create your views here.

def index(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    """Takes an request as a parameter and gives the count of pageview objects as reponse"""
    return HttpResponse(PageView.objects.count())

def image_view(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 

        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = ImageForm() 
    return render(request, 'PyGallery/gallery.html', {'form' : form}) 


def success(request):
    return HttpResponse(PageView.objects.count())