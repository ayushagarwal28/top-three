from django import forms
from .models import Poll, Choice

class PollForm(forms.ModelForm):
    choice = forms.CharField(max_length = 100,
                               label = 'Choice 1',
                               min_length = 1,
                               widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Player Unknown\'s Battle Grounds - PUBG'}))

    choice1 = forms.CharField(max_length = 100,
                               label = 'Choice 2',
                               min_length = 1,
                               widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Call Of Duty - COD'}))

    choice2 = forms.CharField(max_length = 100,
                               label = 'Choice 3',
                               min_length = 1,
                               widget = forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Getting Over It!'}))

    class Meta:
        model = Poll
        fields = ['text',]
        widgets = {
            'text' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Top 3 2019 PC Games'})
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
        widgets = {
            'choice_text' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Add your choice'})
        }
