from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<str:collection>/store-detail/', views.store_detail, name="store-detail"),
    path('<int:product_id>/product-detail/', views.product_detail, name="product-detail"),
    path('<str:product_sku>/shopping-cart/', views.shopping_cart, name="shopping-cart"),
    path('<str:order_ref>/<str:group_order_ref>/', views.new_order_home, name="new-order-home"),
    path('<str:order_ref>/check-out/', views.check_out, name="check-out"),
]
