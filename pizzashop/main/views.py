from django.shortcuts import render
from menu.models import Pasta, Pizza
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics
from rest_framework.response import Response


class TestRenderer(generics.ListAPIView):  # Test renderer for main.html
    queryset = Pizza.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.objects = self.get_queryset()
        return Response({'food': self.objects}, template_name='main.html')
