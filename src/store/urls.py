from django.urls import path

from . import views

urlpatterns = [
    path('home-page/', views.home, name="home"),
]
