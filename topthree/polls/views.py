from django.shortcuts import render
from .models import Poll

# Create your views here.

def polls_list(request):
    polls = Poll.objects.all();
    context = {'polls' : polls}
    return render(request, 'polls/polls_list.html', context)
