from django.shortcuts import render
from menu.models import Pasta, Pizza, Salad, Drinks, Coctail, Garnier, Subs
from . import serializers
from rest_framework import generics


class PastaList(generics.ListAPIView):
    queryset = Pasta.objects.all()
    serializer_class = serializers


class PastaDetail(generics.RetrieveAPIView):
    queryset = Pasta.objects.all()
    serializer_class = serializers


class PizzaList(generics.ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = serializers


class PizzaDetail(generics.RetrieveAPIView):
    queryset = Pizza.objects.all()
    serializer_class = serializers


class SaladList(generics.ListAPIView):
    queryset = Salad.objects.all()
    serializer_class = serializers


class SaladDetail(generics.RetrieveAPIView):
    queryset = Salad.objects.all()
    serializer_class = serializers


class DrinksList(generics.ListAPIView):
    queryset = Drinks.objects.all()
    serializer_class = serializers


class DrinksDetail(generics.RetrieveAPIView):
    queryset = Drinks.objects.all()
    serializer_class = serializers


class CoctailList(generics.ListAPIView):
    queryset = Coctail.objects.all()
    serializer_class = serializers


class CoctailDetail(generics.RetrieveAPIView):
    queryset = Coctail.objects.all()
    serializer_class = serializers


class GarnierList(generics.ListAPIView):
    queryset = Garnier.objects.all()
    serializer_class = serializers


class GarnierDetail(generics.RetrieveAPIView):
    queryset = Garnier.objects.all()
    serializer_class = serializers


class SubsList(generics.ListAPIView):
    queryset = Subs.objects.all()
    serializer_class = serializers


class SubsDetail(generics.RetrieveAPIView):
    queryset = Subs.objects.all()
    serializer_class = serializers