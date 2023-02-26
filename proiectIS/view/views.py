# HttpResponse is used to
# pass the information
# back to view
import filecmp
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse

from django.core.files.storage import FileSystemStorage # pt inccarcare fisiere
from django import forms
#tutorial2
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from proiectIS.model.forms import UploadPDFForm
from django.core.files.base import ContentFile

from proiectIS.model.models import documentPDFModel

from django.core.files.base import ContentFile


from cryptography.fernet import Fernet

KEY = b'xZ0Yw6heUGrF0KwDt7V3IBAY-ZztiHtMrm6kmiuScGM=' 
# Defining a function which
# will receive request and
# perform task depending
# upon function definition
def hello_world(request):
    # This will return Hello Geeks
    # string as HttpResponse
    return HttpResponse("Hello World!")

# #tutorial2: https://www.youtube.com/watch?v=1UvTNMH7zDo&ab_channel=GeeksforGeeks   
def home(request):
   return HttpResponse("Hello i am working!")

def signup (request):
   if request.method == "POST":
      username = request.POST['username']  #username e name inhtml
      fname = request.POST['fname']
      lname = request.POST['lname']
      email = request.POST['email']
      occupation = request.POST['occu']
      pass1 = request.POST['pass1']
      pass2 = request.POST['pass2']

      myuser = User.objects.create_user(username, email, pass1)
      myuser.first_name = fname
      myuser.last_name = lname

      myuser.save()

      messages.success(request, "Your account has been successfully created")
      return redirect('signin')

   
   return render(request, 'authentication/signup.html')




def signin (request):
   if request.method == 'POST':
      username = request.POST['username']
      pass1 = request.POST['pass1']
      #documentPDFModel.objects.all().delete() ####### DECOMENTEZI CAND VR SA STERGI PATH URILE DIN BAZA DE DATE CATRE PDF URI

      user = authenticate(username = username, password = pass1)

      if user is not None:
         login(request, user)
         fname = user.first_name
         return redirect('techcare')
   
         #return render(request, "authentication/index.html", {'fname': fname})

      else:
         messages.error(request, 'Invalid Credentials, Please try again')
         return redirect('home')

   return render(request, 'authentication/signin.html')

def signout (request):
   return render(request, 'authentication/signout.html')
def index(request):
    return render(request, 'authentication/index.html')
# #
def techcare(request):
   return render(request, 'app/techcare.html') 

def hello_worldHTML(request):
   return render(request, 'helloWorld.html')

def components(request):
   return render(request, 'app/components.html')

def services(request):
   return render(request, 'app/services.html')

# def documentlist(request):
#    documents = documentPDFModel.objects.all()
#   # return render(request, 'other_documents.html', {'documents': documents})
#    return render(request, 'app/documentlist.html',  {'documents': documents})

def documentlist(request):  
    documents = documentPDFModel.objects.all()
    cipher_suite = Fernet(KEY)
    decrypted_documents = []
    for document in documents:
      pdf_bytes = document.pdf.read()
      decrypted_pdf = cipher_suite.decrypt(pdf_bytes)
      with open(f'zfilebfr/{document.title}.pdf', 'wb') as f: 
        f.write(decrypted_pdf)
      decrypted_doc = {'url':f'view/{document.title}.pdf','name':document.title} 
      decrypted_documents.append(decrypted_doc)
    context = {'documents': decrypted_documents}
    return render(request, 'app/documentlist.html', context)



def documents(request):
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_bytes = request.FILES['pdf'].read()
            cipher_suite = Fernet(KEY)
            cipher_pdf = cipher_suite.encrypt(pdf_bytes)
            pdf_file = ContentFile(cipher_pdf, name=request.FILES['pdf'].name)
            pdf_model = form.save(commit=False)
            pdf_model.pdf = pdf_file
            pdf_model.save()
            return HttpResponse('The file is saved')
    else:
        form = UploadPDFForm()
    context = {'form':form}   
    return render(request, 'app/documents.html', context)

def view_pdf(request, title):
    file_path = f'zfilebfr/{title}.pdf'
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = f'inline; filename="{title}.pdf"'
    return response

# def documents(request): #bookuploadview
#    if request.method == 'POST':
      
#       form = UploadPDFForm(request.POST, request.FILES)
#       if form.is_valid():
#          form.save()
#          return HttpResponse('The file is saved')
#    else:
#       form = UploadPDFForm()
#       context = {
#             'form':form,
#         }   
  
#    return render(request, 'app/documents.html', context)

