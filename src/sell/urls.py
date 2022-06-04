from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="sell-home"),
    path('<str:product_sku>/products/', views.products_list, name="products-list"),
    path('add-products/', views.add_product, name="add-product"),
]
