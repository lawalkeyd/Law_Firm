from django.db import models
from accounts.models import UserAccount

# Create your models here.
gender_choice = (
    ('male', 'Male'),
    ('Female', 'Female')
)

class BackgroundInfo(models.Model):
    university_name = models.CharField(max_length=100)
    law_school_name = models.CharField(max_length=100)
    law_school_degree = models.CharField(max_length=100)


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
    grade_of_post = models.CharField(max_length=45)
    first_time_scale_due_year = models.IntegerField(null=True, blank=True)
    second_time_scale_due_year = models.IntegerField(null=True, blank=True)
    promotion_due_year = models.DateField(null=True, blank=True)
    expected_retirement_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.category


class PersonalInfo(models.Model):
    name = models.CharField(max_length=45)
    photo = models.ImageField()
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=45)
    nationality_choice = (
        ('Nigerian', 'Nigerian'),
        ('Others', 'Others')
    )
    nationality = models.CharField(max_length=45, choices=nationality_choice)
    religion_choice = (
        ('Christianity', 'Christianity'),
        ('Islam', 'Islam'),
        ('Others', 'Others')
    )
    religion = models.CharField(max_length=45, choices=religion_choice)
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    blood_group_choice = (
        ('a+', 'A+'),
        ('o+', 'O+'),
        ('b+', 'B+'),
        ('ab+', 'AB+'),
        ('a-', 'A-'),
        ('o-', 'O-'),
        ('b-', 'B-'),
        ('ab-', 'AB-')
    )
    blood_group = models.CharField(choices=blood_group_choice, max_length=5)
    driving_license_passport = models.IntegerField(unique=True)
    phone_no = models.CharField(max_length=11, unique=True)
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
    education = models.ForeignKey(BackgroundInfo, on_delete=models.CASCADE, null=True)
    job = models.ForeignKey(JobInfo, on_delete=models.CASCADE, null=True)
    is_delete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    login_details = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name              