from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from polls.models import Contact
import datetime

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save()
            messages.success(request, 'We have received your feedback. Thank you!', extra_tags = 'mt-1 alert alert-success alert-dismissible fade show')
            return redirect('polls:list')
    else:
        form = ContactForm(auto_id = '%s')
        return render(request, 'contact.html', {'form': form})
