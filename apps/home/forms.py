from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


# create a ModelForm


class UploadForm(forms.ModelForm):
    print('upload form')

    # specify the name of model to use
    class Meta:
        model = Video
        fields = ['title', 'video', 'pos']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control'}),
            'pos': forms.Select(attrs={'class': 'form-control'}),
        }