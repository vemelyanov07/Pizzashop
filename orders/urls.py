from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartListView.as_view(), name='cart'),
    path('orders/place/', views.OrderListView.as_view(), name='order_place'),
]
