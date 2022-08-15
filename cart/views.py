from django.shortcuts import render
from django.views.generic import TemplateView


class CartPageView(TemplateView):
    template_name = 'cart/cart.html'
