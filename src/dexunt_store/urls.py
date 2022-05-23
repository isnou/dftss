from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<char:collection>/store-detail/', views.store_detail, name="store_detail"),

]
