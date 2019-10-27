from django import forms
from polls.models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(label = "Name",
                           widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter your name'}))

    email = forms.EmailField(label = "Email",
                             widget = forms.EmailInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter your Email'}))

    message = forms.CharField(label = "",
                              widget = forms.Textarea(attrs = {'class' : 'form-control', 'placeholder' : 'Enter your message'}))

    class Meta:
        model = Contact
        fields = '__all__'
