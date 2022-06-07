from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="store-home"),
    path('<str:collection>/store/', views.store, name="store"),
]
