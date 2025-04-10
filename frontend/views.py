from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def links(request):
    return render(request, 'links.html')

def projects(request):
    return render(request, 'projects.html')
