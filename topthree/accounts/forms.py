from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages

class UserRegistrationForm(forms.Form):
    error_css_class = 'error'

    username = forms.CharField(max_length = 100,
                               widget = forms.TextInput(attrs = {'class' : 'form-control', 'type' : 'text', 'placeholder' : 'Username:'}))

    email = forms.EmailField(widget = forms.EmailInput(attrs = {'class' : 'form-control', 'placeholder' : 'john@smith.com', 'type' : 'email', 'name' : 'email'}))

    password1 = forms.CharField(
                                max_length = 100,
                                min_length = 5,
                                label = 'Enter Password',
                                widget = forms.PasswordInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Password', 'type' : 'password', 'autocomplete' : 'off', 'autofocus' : 'autofocus'}))

    password2 = forms.CharField(
                                max_length = 100,
                                min_length = 5,
                                label = 'Confirm Password',
                                widget = forms.PasswordInput(attrs = {'class' : 'form-control', 'placeholder' : 'Re-enter Password', 'type' : 'password', 'autocomplete' : 'off', 'autofocus' : 'autofocus'}))


    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email = email)
        if qs.exists():
            # messages.success('Email is already registered.', extra_tags = 'mt-1 alert alert-success alert-dismissible fade show')
            raise ValidationError('Email is already registered.')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise ValidationError('Username already taken.')
        return username
    
    def clean_password2(self):
        p1 = self.cleaned_data['password1']
        p2 = self.cleaned_data['password2']
        if p1 and p2:
            if p1 != p2:
                raise ValidationError('Passwords Do Not Match')
        return p2
