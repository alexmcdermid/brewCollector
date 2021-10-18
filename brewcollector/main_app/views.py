from django.shortcuts import render
from .models import Brew

# Create your views here.

from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def brews_index(request):
    brews = Brew.objects.all()
    return render(request, 'brews/index.html', {'brews': brews})

def brews_detail(request, brew_id):
    brew = Brew.objects.get(id=brew_id)
    return render(request, 'brews/detail.html', {'brew': brew})