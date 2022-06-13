from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="store-home"),
    path('<str:collection>/store/', views.store, name="store"),
    path('<int:product_id>/product/', views.product, name="product"),
    path('<int:product_id>/order/', views.order, name="order"),
    path('<str:sku>/delete-product/', views.delete_product, name="delete-product"),
    path('<str:sku>/add-quantity/', views.add_quantity, name="add-quantity"),
    path('<str:sku>/delete-product-to-home/', views.delete_product_to_home, name="delete-product-to-home"),
    path('show-cart/', views.show_cart, name="show-cart"),

]
