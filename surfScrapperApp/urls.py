from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('registerForm/', views.registerForm, name='registerForm')
]