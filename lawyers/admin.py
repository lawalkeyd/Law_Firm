from django.contrib import admin
from .models import BackgroundInfo, JobInfo, PersonalInfo

# Register your models here.
admin.site.register(BackgroundInfo)
admin.site.register(JobInfo)
admin.site.register(PersonalInfo)