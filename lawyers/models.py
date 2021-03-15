from django.db import models

# Create your models here.
gender_choice = (
    ('male', 'Male'),
    ('Female', 'Female')
)
class PersonalInfo(models.Model):
    name = models.CharField(max_length=54)
    photo = models.ImageField()
    gender = models.CharField(choices=gender_choice, max_length=7)
    email = models.CharField(max_length=255, unique=True)
    father_name = models.CharField(max_length=45)
    mother_name = models.CharField(max_length=45)
    marital_status_choice = (
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('separated', 'Separated'),
        ('divorced', 'Divorced'),
        ('single', 'Single')
    )
    marital_status = models.CharField(choices=marital_status_choice, max_length=10)

    def __str__(self):
        return self.name

class JobInfo(models.Model):
    lawyer_class = (
        ('non law', 'Non law'),
        ('paralegal', 'Paralegal'),
        ('associate', 'Associate'),
        ('partner', 'Partner'),
        ('Named', 'Named'),
    )
    category = models.CharField(choices=lawyer_class, max_length=45)
    joning_date = models.DateField()
    university_name = models.CharField(max_length=100)
    law_school_name = models.CharField(max_length=100)
    scale = models.IntegerField()
    grade_of_post = models.CharField(max_length=45)
    first_time_scale_due_year = models.IntegerField()
    second_time_scale_due_year = models.IntegerField()
    promotion_due_year = models.IntegerField()
    recreation_leave_due_year = models.IntegerField()
    expected_retirement_year = models.IntegerField()

    def __str__(self):
        return self.category

        