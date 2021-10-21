from django.shortcuts import redirect, render
from .models import Brew, Ingredient,Locations
from .forms import LocationsForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def brews_index(request):
    #brews = Brew.objects.all()
    brews = Brew.objects.filter(user=request.user)
    return render(request, 'brews/index.html', {'brews': brews})

@login_required
def brews_detail(request, brew_id):
    brew = Brew.objects.get(id=brew_id)
    return render(request, 'brews/detail.html', {'brew': brew})


def brews_new(request):
    return render(request,'brews/new.html', {})

#old brews create
@login_required
def brews_create(request):
    brew = Brew.objects.create(
        name = request.POST['name'],
        beerType = request.POST['beerType'],
        brewery = request.POST['brewery'],
        ibu = request.POST['ibu'],
        alcoholPercent = request.POST['alcoholPercent'],
        price = request.POST['price']
        #user = request.user this is how we would do it with not createview
    )

    return redirect(f'/brews/{brew.id}')

class BrewCreate(LoginRequiredMixin,CreateView):
  model = Brew
  fields = ['name', 'beerType', 'brewery', 'ibu','alcoholPercent','price']
  
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

@login_required
def brews_delete(request, brew_id):
    brew = Brew.objects.get(id=brew_id)
    brew.delete()
    return redirect('/brews')

@login_required
def brews_edit(request, brew_id):
    brew = Brew.objects.get(id=brew_id)
    return render(request, 'brews/edit.html', {'brew':brew})

@login_required
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

@login_required
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

@login_required
def add_location(request, brew_id):
    form = LocationsForm(request.POST)
    if form.is_valid():
        new_location = form.save(commit=False)
        new_location.brew_id = brew_id
        new_location.save()
    return redirect('detail', brew_id=brew_id)

@login_required
def assoc_ing(request, brew_id, ingredient_id):
  # Note that you can pass a toy's id instead of the whole object
  Brew.objects.get(id=brew_id).ingredients.add(ingredient_id)
  return redirect('detail', brew_id=brew_id)

@login_required
def unassoc_ing(request, brew_id, ingredient_id):
  # Note that you can pass a toy's id instead of the whole object
  Brew.objects.get(id=brew_id).ingredients.remove(ingredient_id)
  return redirect('detail', brew_id=brew_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)