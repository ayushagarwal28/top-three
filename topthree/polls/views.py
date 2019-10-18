from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Poll

# Create your views here.

def polls_list(request):
    polls = Poll.objects.all();
    context = {'polls' : polls}
    return render(request, 'polls/polls_list.html', context)

def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id = poll_id)
    context = {'poll' : poll}
    return render(request, 'polls/poll_detail.html', context)
