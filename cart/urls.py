from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartPageView.as_view(), name='cart'),
]
