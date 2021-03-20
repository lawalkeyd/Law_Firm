from django import forms
from .models import BackgroundInfo, PersonalInfo, JobInfo
from accounts.models import UserAccount


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        exclude = {'education', 'job', 'is_delete', 'login_details'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'place_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'nationality': forms.Select(attrs={'class': 'form-control'}),
            'religion': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'driving_license_passport': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),

        }




class EducationInfoForm(forms.ModelForm):
    class Meta:
        model = BackgroundInfo
        fields = '__all__'
        widgets = {
            'university_name': forms.TextInput(attrs={'class': 'form-control'}),
            'law_school_name': forms.TextInput(attrs={'class': 'form-control'}),
            'law_school_degree': forms.TextInput(attrs={'class': 'form-control'}),
        }



class JobInfoForm(forms.ModelForm):
    class Meta:
        model = JobInfo
        fields = '__all__'
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'joining_date': forms.DateInput(attrs={'class': 'form-control'}),
            'promotion_due_year': forms.DateInput(attrs={'class': 'form-control'}),
            'expected_retirement_date': forms.DateInput(attrs={'class': 'form-control'}),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields  = '__all__'

