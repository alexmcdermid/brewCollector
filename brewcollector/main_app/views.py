from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>its brewtime')

def about(request):
    return render(request, 'about.html')

class Brew:
    def __init__(self, name):
        self.name = name

brews = [
    Brew('Pale Ale'),
    Brew('IPA'),
    Brew('Summer Ale')
]

def brews_index(request):
    return render(request, 'brews/index.html', {'brews': brews})