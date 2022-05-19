from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:key_id>/detail/', views.detail, name="detail"),
    path('posts-json/<int:num_posts>/', PostJsonListView.as_view(), name='posts-json-view'),
]