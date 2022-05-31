from django.urls import path

from . import views

urlpatterns = [
    path('', views.manager_home, name="manager-home"),
    path('orders-list/', views.orders_list, name="orders-list"),
    path('<str:group_order_ref>/orders-details/', views.orders_details, name="orders-details"),
    path('<str:group_order_ref>/delete-orders/', views.delete_orders, name="delete-orders"),
    path('<str:group_order_ref>/<str:order_ref>/delete-order/', views.delete_order, name="delete-order"),
]
