from django.contrib import admin

from .models import Brew, Ingredient,Locations

# Register your models here.
admin.site.register(Brew)
admin.site.register(Locations)
admin.site.register(Ingredient)