from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist

def registration(request):
    if request.method == 'POST':
        form1 = userform(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['username']
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            return HttpResponseRedirect('/registration/')
    else:
        form1 = userform()
    return render(request, 'registration.html', {'frm':form1})

def login(request):
    if request.method=="POST":
        username = request.POST['user']
        password = request.POST['pas']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/dashboard/')
            else:
                messages.error(request, 'Username and Password did not matched')
        except auth.ObjectNotExist:
            print("Invalid user")
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contact.html')

def attendence(request):
    return render(request, 'attendence.html')

def about(request):
    return render(request, 'about.html')

def faculty(request):
    return render(request, 'faculty.html')

def tt(request):
    return render(request, 'tt.html')