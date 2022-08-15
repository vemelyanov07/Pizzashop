from rest_framework import serializers
from menu.models import Pasta, Pizza, Salad, Drinks, Coctail, Garnier, Subs


class PastaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasta
        fields = ["name", "price"]


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ["name", "medium_price", "large_price"]   


class SaladSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salad
        fields = ["name", "ingredients", "price"]   


class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ["name", "ingredients", "price"] 


class CoctailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coctail
        fields = ["name", "ingredients", "price"] 


class GarnierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garnier
        fields = ["name", "price"] 


class SubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subs
        fields = ["name", "price"] 