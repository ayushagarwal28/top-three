from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from accounts.forms import UserRegistrationForm
from polls.models import Poll
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password= password)
        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'home')
            return redirect(redirect_url)
        else:
            messages.error(request, 'Wrong username or password', extra_tags = 'mt-1 alert alert-danger alert-dismissible fade show')
    return render(request, 'accounts/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email = email, password = password)
            messages.success(request, 'User succesfully registered!', extra_tags = 'mt-1 alert alert-success alert-dismissible fade show')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm(auto_id = '%s')
    return render(request, 'accounts/register.html', {'form' : form})

@login_required
def details_user(request, username):
    user = get_object_or_404(User, username__iexact = username)
    flag = False
    if request.user.get_username() == username:
        flag = True
    print(user.poll_set.all())
    return render(request, 'accounts/details.html', {'polls' : user.poll_set.all(), 'flag' : flag, 'username' : username})

@login_required
def delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.user != poll.owner:
        return redirect('/')
    if request.method == "POST":
        poll.delete()
        messages.success(
                        request,
                        'Poll Deleted Successfully',
                        extra_tags='alert alert-success alert-dismissible fade show'
                        )
        return redirect('polls:list')
    return render(request, 'accounts/delete_poll_confirm.html', {'poll':poll})
