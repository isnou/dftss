from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="sell-home"),
    path('products/', views.products_list, name="products-list"),
]