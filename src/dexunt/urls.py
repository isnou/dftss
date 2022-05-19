from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:key_id>/detail/', views.detail, name="detail"),
    path('index/', views.index, name='index'),
    path('load_more/', views.load_more, name='load_more'),
]