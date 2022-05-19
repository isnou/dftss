from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:key_id>/detail/', views.detail, name="detail"),
    path('', views.MainView, name='main-view'),
    path('posts-json/<int:num_posts>/', views.PostJsonListView, name='posts-json-view'),
]