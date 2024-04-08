 
# api/urls.py
from django.urls import path
from . import views  

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user/', views.User, name='user'),
    path('referrals/', views.referrals, name='referrals'),
]