from django import forms
from .models import *

class ImageForm(forms.modelForm):

    class Meta:

        model = Images
        field = ['name', 'image']