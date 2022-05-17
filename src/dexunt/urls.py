from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:key_id>/', views.home, name="home"),
    path('detail', views.detail, name="detail"),
]