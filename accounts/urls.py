from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfilePageView.as_view(), name='profile'),
    path('login/', views.LoginPageView.as_view(), name='login'),
]
