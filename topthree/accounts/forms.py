from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length = 100, label = 'Username')
    password = forms.CharField(max_length = 100, label = 'Password')
