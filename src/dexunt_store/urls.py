from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<str:collection>/store-detail/', views.store_detail, name="store-detail"),
    path('<int:product_id>/product-detail/', views.product_detail, name="product-detail"),

]
