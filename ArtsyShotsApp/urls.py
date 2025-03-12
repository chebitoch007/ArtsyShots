
from django.contrib import admin
from django.urls import path
from ArtsyShotsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('starter-page/', views.starter, name='starter-page'),
    path('', views.index, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery-single/', views.single, name='gallery-single'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
