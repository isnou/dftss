from django.urls import path

from . import views

urlpatterns = [
    path('', views.manager_home, name="manager-home"),
    path('all-orders-list/', views.all_orders_list, name="all-orders-list"),
]
