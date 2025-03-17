
from django.contrib import admin
from django.urls import path
from ArtsyShotsApp import views
from .views import register_view, login_view, logout_view
from django.contrib.auth import views as auth_views
from ArtsyShotsApp.views import register_view
from .views import register  # Import the register view properly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('starter-page/', views.starter, name='starter-page'),
    path('home/', views.index, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery-single/', views.single, name='gallery-single'),
    path('services/', views.services, name='services'),
    path('hiring/', views.hiring, name='hiring'),
    path('pay', views.pay, name='pay'),
    path('register_view/', views.register_view, name='register_view'),
    path('', views.register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),



]
