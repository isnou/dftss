from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:key>/store-detail/', views.store_detail, name="store_detail"),

]
