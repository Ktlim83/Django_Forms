from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    
    context = {}
    
    return render(request, "index.html", context)  
