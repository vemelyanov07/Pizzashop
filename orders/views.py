from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated

class CartListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(template_name="orders/cart.html")

class OrderListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(template_name="orders/order_place.html")