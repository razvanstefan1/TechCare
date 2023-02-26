"""proiectIS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static



#importing hello world function from views.py file

from proiectIS.view.views import *
from proiectIS.view.views import techcare, documents, services, components, documentlist

urlpatterns = [
    path('admin/', admin.site.urls),

    # #path uri pt acest tutorial: https://www.youtube.com/watch?v=1UvTNMH7zDo&ab_channel=GeeksforGeeks
    path('',index, name = 'index'),   
    path('signup', signup, name = 'signup'),   
    path('signin', signin, name='signin'),  #!!!!!!!!!!!!!!! FARA name = 'signin' nu functioneaza redirectul de la signup 
    path('signout', signout, name = 'signout'), 
    path('techcare', techcare, name = 'techcare'),
    path('documents', documents, name = 'documents'),
    path('services', services, name = 'services'),
    path('components', components, name = 'components'),
    path('documentlist', documentlist, name = 'documentlist'),
    path('viewpdf/<str:title>', view_pdf, name='view_pdf'),


    #
	#mapping url to hello world function
	path('geek/' , hello_world),
   
]

if settings.DEBUG:             ####
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) ####
