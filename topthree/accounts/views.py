from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from accounts.forms import UserRegistrationForm

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password= password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Wrong username or password')
    return render(request, 'accounts/login.html', {})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, password = password)
            messages.success(request, 'User succesfully registered!')
            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form' : form})
