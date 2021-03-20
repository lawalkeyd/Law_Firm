from django.urls import path
from . import views

urlpatterns = [
    path('registration', views.lawyer_registration, name='lawyer_registration'),
]