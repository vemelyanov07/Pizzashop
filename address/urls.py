from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddressPageView.as_view(), name='address'),
    path('change_address/', views.ChangeAddressPageView.as_view(), name='change_address'),
]
