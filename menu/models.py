from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    medium_price = models.DecimalField(max_digits=2, decimal_places=2) 
    large_price = models.DecimalField(max_digits=2, decimal_places=2) 

    def __str__(self):
        return self.name


class Salad(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=2, decimal_places=2) 

    def __str__(self):
        return self.name


class Pasta(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=2, decimal_places=2) 

    def __str__(self):
        return self.name


class Garnier(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mass = models.IntegerField()

    def __str__(self):
        return self.name

class Cocktail(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()

    def __str__(self):
        return self.name

class Drinks(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()

    def __str__(self):
        return self.name

class Subs(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mass = models.IntegerField()

    def __str__(self):
        return self.name