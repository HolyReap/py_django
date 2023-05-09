from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from os import listdir

# Create your views here.

def home_page_view(request):
    return HttpResponse("This is the Home page.")

def current_time_view(request):
    dt = datetime.now()
    return HttpResponse(dt)

def workdir_view(request): 
    list = listdir('.')
    res = ''
    for item in list:
        res += f"<div>{item}</div>"
    return HttpResponse(res)
