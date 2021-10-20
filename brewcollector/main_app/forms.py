from django.forms import ModelForm
from .models import Locations

class LocationsForm(ModelForm):
  class Meta:
    model = Locations
    fields = ['stock', 'date', 'location']