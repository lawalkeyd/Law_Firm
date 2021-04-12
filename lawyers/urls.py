from django.urls import path
from . import views

urlpatterns = [
    path('registration', views.lawyer_registration, name='lawyer_registration'),
    path('list', views.lawyer_list, name='lawyer_list'),
    path('profile/<id>', views.lawyer_profile, name='lawyer_profile'),
]