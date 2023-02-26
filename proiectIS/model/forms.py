from django import forms
#from . import models
from .models import documentPDFModel

class UploadPDFForm(forms.ModelForm):
   # encryption_key = forms.CharField(widget=forms.PasswordInput) ####
    class Meta:
        model = documentPDFModel  #ebooksmodel
        fields = ('title', 'pdf',)

# class EncryptionKeyForm(forms.Form): ####
#     encryption_key = forms.CharField(widget=forms.PasswordInput) ####