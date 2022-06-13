from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="store-home"),
    path('<str:collection>/store/', views.store, name="store"),
    path('<int:product_id>/product/', views.product, name="product"),
    path('<int:product_id>/order/', views.order, name="order"),
    path('<str:sku>/delete/', views.delete_product, name="delete-product"),
    path('shopping-cart/', views.shopping_cart, name="shopping-cart"),

]
