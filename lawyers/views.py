from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import forms
from .models import *

# Create your views here.


@login_required(login_url='login')
def lawyer_registration(request):
    form = forms.PersonalInfoForm()
    education_form = forms.EducationInfoForm()
    job_form = forms.JobInfoForm()
    login_form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.PersonalInfoForm(request.POST, request.FILES)
        education_form = forms.EducationInfoForm(request.POST)
        job_form = forms.JobInfoForm(request.POST)
        login_form = forms.LoginForm(request.POST)
        if form.is_valid() and education_form.is_valid() and job_form.is_valid() and login_form.is_valid():
            education_info = education_form.save()
            job_info = job_form.save()
            login_info = login_form.save()
            personal_info = form.save(commit=False)
            personal_info.education = education_info
            personal_info.job = job_info
            personal_info.login_details = login_info
            personal_info.save()
            return redirect('home')

    context = {
        'form': form,
        'education_form': education_form,
        'job_form': job_form,
        'login_form': login_form
    }
    return render(request, 'lawyers/lawyer-registration.html', context)

