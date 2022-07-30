from django.urls import path, include
from . import views


app_name = 'test_main'
urlpatterns = [
    path('test_main/', views.TestRenderer.as_view(), name='pizza'),  # for testing main page, delete after review
]