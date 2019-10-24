from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length = 100,
                               widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'John Smith', 'type' : 'text', 'autocomplete' : 'off', 'autofocus' : 'autofocus', 'aria-describedby' : 'username'}))

    email = forms.EmailField(widget = forms.EmailInput(attrs = {'class' : 'form-control', 'placeholder' : 'john@smith.com', 'type' : 'email', 'autocomplete' : 'off', 'autofocus' : 'autofocus'}))

    password1 = forms.CharField(
                                max_length = 100,
                                min_length = 5,
                                widget = forms.PasswordInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Password', 'type' : 'password', 'autocomplete' : 'off', 'autofocus' : 'autofocus'}))

    password2 = forms.CharField(
                                max_length = 100,
                                min_length = 5,
                                widget = forms.PasswordInput(attrs = {'class' : 'form-control', 'placeholder' : 'Re-enter Password', 'type' : 'password', 'autocomplete' : 'off', 'autofocus' : 'autofocus'}))


    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email = email)
        if qs.exists():
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
