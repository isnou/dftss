from django.urls import path

from . import views

urlpatterns = [
    path('', views.manager_home, name="manager-home"),
    path('orders/', views.orders, name="orders"),
    path('orders-details/', views.orders_details, name="orders-details"),
]
