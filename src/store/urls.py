from django.urls import path

from . import views

urlpatterns = [
    path('<str:product_sku>/', views.home, name="store-home"),
]
