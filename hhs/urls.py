from django.contrib import admin
from django.urls import path, include
from hhs import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home', views.home, name = 'home'),
    path('rooms', views.rooms, name = 'rooms'),
    path('sofa', views.sofa, name = 'sofa'),
    path('kitchen', views.kitchen, name = 'kitchen'),
    path('bathroom', views.bathroom, name = 'bathroom'),
    path('toilet', views.toilet, name = 'toilet'),
    path('carpet', views.carpet, name = 'carpet'),
    path('car', views.car, name = 'car'),
    path('login', views.login, name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('know', views.know, name = 'know'),
    path('mailerror', views.mailerror, name = 'mailerror'),
    path('logout', views.logout, name = 'logout'),
    
]
