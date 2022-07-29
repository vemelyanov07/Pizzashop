from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile.as_view(), name='profile')
]

urlpatterns = [
    path('login/', views.LoginPageView.as_view(), name='login'),
]
