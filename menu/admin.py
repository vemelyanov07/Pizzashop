from django.contrib import admin
from .models import Pizza, Salad, Pasta, Garnier, Drinks, Cocktail, Subs
# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'medium_price', 'large_price')


class SaladAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class PastaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class DrinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'volume')


class CocktailAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'volume')


class GarnierAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'mass')


class SubsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'mass')

admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Salad, SaladAdmin)
admin.site.register(Pasta, PastaAdmin)
admin.site.register(Drinks, DrinksAdmin)
admin.site.register(Garnier, GarnierAdmin)
admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(Subs, SubsAdmin)