from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Brew(models.Model):
    name = models.CharField(max_length=100)
    beerType = models.CharField(max_length=100)
    brewery = models.CharField(max_length=100)
    ibu = IntegerField()
    alcoholPercent = IntegerField()
    price = IntegerField()

    def __str__(self):
        return self.name