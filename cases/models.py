from django.db import models

# Create your models here.

class Cases(models.Model):
    title = models.CharField(max_length=126)
    