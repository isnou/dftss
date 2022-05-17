from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:key_id>/', views.home, name="home"),
    path('detail/<int:key_id>', views.detail, name="detail"),
]