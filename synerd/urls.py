from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),    
    path('form/', views.form, name='form'),
    path('otherform/', views.otherform, name='otherform'),
    path('members/', views.members, name='members')
]