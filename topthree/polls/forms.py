from django import forms
from .models import Poll

class PollForm(forms.ModelForm):
    choice = forms.CharField(max_length = 100,
                               label = 'Choice',
                               min_length = 1,
                               widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Player Unknown\'s Battle Grounds - PUBG'}))

    choice1 = forms.CharField(max_length = 100,
                               label = 'Choice',
                               min_length = 1,
                               widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Call Of Duty - COD'}))

    class Meta:
        model = Poll
        fields = ['text',]
        widgets = {
            'text' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Top 3 2019 PC Games'})
        }
