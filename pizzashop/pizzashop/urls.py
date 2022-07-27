from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('address/', include('address.urls')),
    path('cart/', include('cart.urls')),
    path('main/', include('main.urls')),
    path('menu/', include('menu.urls')),
]
