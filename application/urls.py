from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.Home, name='Home'),  # Home page URL
    path('product/', views.product, name='product'),  # Product page URL
    path('login/', views.login, name='login'),  # Login page URL
    path('register/', views.register, name='register'),  # Register page URL
    path('signout/', views.signout, name='signout'),  # Sign out URL
    path('order_windows/', views.order_windows, name='order_windows'),  # Order page URL
    path('UserDashboard/', views.UserDashboard, name='UserDashboard'),  # User Dashboard URL
    path('AdminDashboard/', views.AdminDashboard, name='AdminDashboard'),  # Admin Dashboard URL
    path('confirm_order/', views.confirm_order, name='confirm_order'),  # Confirm order URL
    path('pay/<int:order_id>/', views.payment_page, name='payment_page'),
    path('process-payment/<int:order_id>/', views.process_payment, name='process_payment'),

]