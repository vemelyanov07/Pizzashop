from django.urls import path
from . import views


urlpatterns = [
    path('menu/', views.PastaList.as_view()),
    path('menu/<int:pk>/,', views.PastaDetail.as_view()),
    path('menu/', views.PizzaList.as_view()),
    path('menu/<int:pk>/,', views.PizzaDetail.as_view()),
    path('menu/', views.SaladList.as_view()),
    path('menu/<int:pk>/,', views.SaladDetail.as_view()),
    path('menu/', views.DrinksList.as_view()),
    path('menu/<int:pk>/,', views.DrinksDetail.as_view()),
    path('menu/', views.CoctailList.as_view()),
    path('menu/<int:pk>/,', views.CoctailDetail.as_view()),
    path('menu/', views.GarnierList.as_view()),
    path('menu/<int:pk>/,', views.GarnierDetail.as_view()),
    path('menu/', views.SubsList.as_view()),
    path('menu/<int:pk>/,', views.SubsDetail.as_view()),
]