from pyexpat import model
from unicodedata import name
from django.db import models


class Pasta(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return self.name   


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    medium_price = models.DecimalField(max_digits=10, decimal_places=2)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return self.name
    