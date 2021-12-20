from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group_posts/<slug:pk>/', views.group_posts),
] 