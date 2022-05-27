from django.urls import path

from . import views

urlpatterns = [
    path('', views.initial, name="init-home"),
    path('<str:order_ref>/<str:group_order_ref>/welcome/', views.home, name="home"),
    path('<str:collection>/<str:group_order_ref>/store-detail/', views.store_detail, name="store-detail"),
    path('<int:product_id>/<str:group_order_ref>/product-detail/', views.product_detail, name="product-detail"),
    path('<str:product_sku>/<str:group_order_ref>/shopping-cart/', views.shopping_cart, name="shopping-cart"),
    path('<str:order_ref>/check-out/', views.check_out, name="check-out"),
]
