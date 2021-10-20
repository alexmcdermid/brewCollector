from django.shortcuts import redirect, render
from .models import Brew, Ingredient,Locations
from .forms import LocationsForm


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

def brews_new(request):
    return render(request,'brews/new.html', {})

def brews_create(request):
    brew = Brew.objects.create(
        name = request.POST['name'],
        beerType = request.POST['beerType'],
        brewery = request.POST['brewery'],
        ibu = request.POST['ibu'],
        alcoholPercent = request.POST['alcoholPercent'],
        price = request.POST['price']
    )
    return redirect(f'/brews/{brew.id}')

def brews_delete(request, brew_id):
    brew = Brew.objects.get(id=brew_id)
    brew.delete()
    return redirect('/brews')

def brews_edit(request, brew_id):
    brew = Brew.objects.get(id=brew_id)
    return render(request, 'brews/edit.html', {'brew':brew})

def brews_update(request, brew_id):
    brew = Brew.objects.get(id=brew_id)
    brew.name = request.POST['name']
    brew.beerType = request.POST['beerType']
    brew.brewery = request.POST['brewery']
    brew.ibu = request.POST['ibu']
    brew.alcoholPercent = request.POST['alcoholPercent']
    brew.price = request.POST['price']
    brew.save()
    return redirect(f'/brews/{brew.id}')

def brews_detail(request, brew_id):
    brew = Brew.objects.get(id=brew_id)
    location_form = LocationsForm()
    locations = Locations.objects.all()
    count = 0
    for location in locations:
        count+=location.stock
    
    ingredients_brew_doesnt_have = Ingredient.objects.exclude(id__in = brew.ingredients.all().values_list('id'))
    return render(request, 'brews/detail.html', {
        'brew': brew, 'location_form': location_form, 'count': count, 'ingredients':ingredients_brew_doesnt_have
    })

def add_location(request, brew_id):
    form = LocationsForm(request.POST)
    if form.is_valid():
        new_location = form.save(commit=False)
        new_location.brew_id = brew_id
        new_location.save()
    return redirect('detail', brew_id=brew_id)


def assoc_ing(request, brew_id, ingredient_id):
  # Note that you can pass a toy's id instead of the whole object
  Brew.objects.get(id=brew_id).ingredients.add(ingredient_id)
  return redirect('detail', brew_id=brew_id)

def unassoc_ing(request, brew_id, ingredient_id):
  # Note that you can pass a toy's id instead of the whole object
  Brew.objects.get(id=brew_id).ingredients.remove(ingredient_id)
  return redirect('detail', brew_id=brew_id)