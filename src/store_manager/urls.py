from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="store-home"),
    path('', views.home, name="store"),
    path('', views.home, name="product"),
    path('', views.home, name="order"),
    path('', views.home, name="delete-product"),
    path('', views.home, name="add-quantity"),
    path('', views.home, name="remove-quantity"),
    path('', views.home, name="delete-product-to-home"),
    path('', views.home, name="show-cart"),
]