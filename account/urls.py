# ACCOUNTS_URLS

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.my_posts, name='profile'),
    # path('edit-profile/<int:id>/', views.editprofile, name='edit-profile'),
]