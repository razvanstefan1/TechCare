from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class documentPDFModel(models.Model): #ebooksmodel
 
    title = models.CharField(max_length = 80)
    pdf = models.FileField(upload_to='pdfs/')
 
    class Meta:
        ordering = ['title']
     
    def __str__(self):
        return f"{self.title}"