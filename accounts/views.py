from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

# Create your views here.

def Userlogin(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context = {'forms': forms}
    return render(request, 'accounts/login.html', context)


def Userlogout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def home(request):
    response = render(request, 'home.html')
    if request.COOKIES.get('visits'):
        value = int(request.COOKIES.get('visits'))
        response.set_cookie('visits', value + 1)
    else:
        response.set_cookie('visits', 1)
    return response         
