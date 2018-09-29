from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *

def dashboard(request):
    obj = feed_back.objects.all()
    return render(request, 'dashboard.html', {'obj':obj})

def feedback1(request):
    if request.method=='POST':
        form = feed_back_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = feed_back_form()
    return render(request, 'feedback.html', {'form':form})