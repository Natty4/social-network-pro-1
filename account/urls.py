from django.urls import re_path, path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

 #re_path(r'^register/', views.register, name='register'),
 path('register/', views.register, name='register'),
 path('edit/', views.edit, name='edit'),
 #path('', views.dashboard, name='dashboard'),
 path('', views.dashboard, name='dashboard'),
 #path('about/', views.about, name='about'),
 path('', include('django.contrib.auth.urls')),

]