
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    # path('home/<int:id>/', views.home, name='home'),
    path('write/', views.newpost, name='write'),
    path('newpost/<int:id>/', views.createdpost, name='createdpost'),
    path('post-detail/<int:id>/', views.post_detail, name='post_detail'),

]
