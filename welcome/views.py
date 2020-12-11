import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, request
from .forms import *

from . import database
from .models import PageView

# Create your views here.

def image_view(request):

    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 

        if form.is_valid(): 
            form.save() 

    else: 
        form = ImageForm() 
    return render(request, 'PyGallery/gallery.html', {'form' : form}) 


