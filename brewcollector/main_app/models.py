from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse
from datetime import date

LOCATIONS = (
    ('N', 'North Vancouver BCL'),
    ('E', 'East Vancouver BCL'),
    ('S', 'South Vancouver BCL'),
    ('W', 'West Vancouver BCL')
)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredients_detail', kwargs={'pk': self.id})    

# Create your models here.
class Brew(models.Model):
    name = models.CharField(max_length=100)
    beerType = models.CharField(max_length=100)
    brewery = models.CharField(max_length=100)
    ibu = IntegerField()
    alcoholPercent = IntegerField()
    price = IntegerField()

    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'brew_id': self.id})
    
    def stocked(self):
        return self.location_set.stock >= 20

class Locations(models.Model):
    stock = models.IntegerField('stock',default=1)
    date = models.DateField('best before date')
    location = models.CharField(max_length=1,choices=LOCATIONS,default=LOCATIONS[0][0])
    brew = models.ForeignKey(Brew, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_location_diplay()} on {self.date}"


