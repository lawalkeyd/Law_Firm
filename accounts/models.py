from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class UserAccount(AbstractUser):
    is_non_law = models.BooleanField(default=False)
    is_par_legal = models.BooleanField(default=False)
    is_asssociate = models.BooleanField(default=False)
    is_partner= models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    photo = models.ImageField(upload_to='admin/')
    gender_select = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(choices=gender_select, max_length=6)
    employee_class = (
        ('non law', 'Non law'),
        ('paralegal', 'Paralegal'),
        ('associate', 'Associate'),
        ('partner', 'Partner'),
        ('Named', 'Named'),
    )
    employee_type = models.CharField(choices=employee_class, max_length=15)

    def __str__(self):
        return self.name