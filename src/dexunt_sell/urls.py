from django.urls import path

from . import views

urlpatterns = [
    path('', views.manager_home, name="manager-home"),
    path('orders/', views.orders_list, name="orders-list"),
    path('orders-details/', views.orders_details, name="orders-details"),
]
