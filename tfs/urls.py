"""tfs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from appt.views import *
from appf.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', registration),
    path('login/', login),
    path('logout/', logout),
    path('dashboard/', dashboard),
    path('feedback/', feedback1),
    path('home/',home),
    path('contacts/',contacts),
    path('attendence/',attendence),
    path('about/',about),
    path('faculty/', faculty),
    path('tt/',tt),
]
