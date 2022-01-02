from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='posts_main'),
    path('group_posts/', views.group_posts, name='post_group'),
]