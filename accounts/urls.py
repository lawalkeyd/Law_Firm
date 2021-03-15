from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.Userlogin, name='login'),
    path('logout', views.Userlogout, name='logout'),
]