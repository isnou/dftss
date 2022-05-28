from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:key_id>/detail/', views.detail, name="detail"),
    path('<int:number>/store/', views.store, name="store"),
    path('best_selling_store/', views.best_selling_store, name="best_selling_store"),
    path('best_rating_store/', views.best_rating_store, name="best_rating_store"),
    path('latest_products/', views.latest_products, name="latest_products"),
    path('<int:item_id>/shopping_cart/', views.shopping_cart, name="shopping_cart"),
    path('<int:shopping_cart_id>/one_order_checkout/', views.one_order_checkout, name="one_order_checkout"),

]
