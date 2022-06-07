from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="store-home"),
    path('<str:product_sku>/', views.home, name="store-home"),
]
