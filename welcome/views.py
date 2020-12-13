import os
from django.forms.forms import Form
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, request
from .forms import *

from . import database
from .models import PageView

# Create your views here.

# url to image = http://django-ex-test.apps-crc.testing/media/images/**image-name**
def image_upload(request):

    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 

        if form.is_valid(): 
            form.save()
            return redirect('image_gallery')

    else: 
        form = ImageForm() 
    return render(request, 'PyGallery/upload.html', {'form' : form}) 

def image_gallery(request):
    image = Images.objects.order_by('timestamp').all()
    return render(request, 'PyGallery/gallery.html', {'images' : image})

