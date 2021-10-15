from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Brew:
    def __init__(self, name, beerType, brewery, ibu, alcoholPercent, price):
        self.name = name
        self.beerType = beerType
        self.brewery = brewery
        self.ibu = ibu
        self.alcoholPercent = alcoholPercent
        self.price = price


brews = [
    Brew('Vancouver Pale Ale','Pale Ale', 'Vancouver Brewing', '20', '5%','2$'),
    Brew('Vancouver IPA','IPA', 'Vancouver Brewing', '80', '8%','4$'),
    Brew('Vancouver Pilsner','Pilsner', 'Vancouver Brewing', '40', '4%','3$')
]

def brews_index(request):
    return render(request, 'brews/index.html', {'brews': brews})