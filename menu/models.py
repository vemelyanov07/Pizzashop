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

class Salad(models.Model):
    name = models.CharField(max_length=50)
    ingredients =  models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Drinks(models.Model):
    name = models.CharField(max_length=50)
    ingredients =  models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Coctail(models.Model):
    name = models.CharField(max_length=50)
    ingredients =  models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Garnier(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Subs(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name



    