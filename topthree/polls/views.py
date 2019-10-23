from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Poll, Choice
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import PollForm, ChoiceForm
import datetime
# Create your views here.

@login_required
def poll_list(request):
    polls = Poll.objects.all();
    context = {'polls' : polls}
    return render(request, 'polls/poll_list.html', context)

@login_required
def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id = poll_id)
    context = {'poll' : poll}
    return render(request, 'polls/poll_detail.html', context)

@login_required
def poll_vote(request, poll_id):
    choice_id = request.POST.get('choice')
    poll = get_object_or_404(Poll, id = poll_id)
    if choice_id:
        choice = Choice.objects.get(id = choice_id)
        choice.votes += 1
        choice.save()
        messages.success(request, 'Your vote has been recorded!', extra_tags = 'mt-1 alert alert-success alert-dismissible fade show')
    else:
        messages.error(request, 'Please caste your vote!', extra_tags = 'mt-1 alert alert-danger alert-dismissible fade show')
        return HttpResponseRedirect(reverse('polls:details', args=(poll_id, )))
    return render(request, 'polls/poll_result.html', {'poll' : poll})

@login_required
def add_poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            new_poll = form.save(commit = False)
            new_poll.pub_date = datetime.datetime.now()
            new_poll.owner = request.user
            new_poll.save()
            new_choice1 = Choice(
                                poll = new_poll,
                                choice_text = form.cleaned_data['choice']
                                ).save()
            new_choice2 = Choice(
                                poll = new_poll,
                                choice_text = form.cleaned_data['choice1']
                                ).save()
            messages.success(request, 'Your poll is now live!', extra_tags = 'mt-1 alert alert-success alert-dismissible fade show')
            return redirect('polls:list')
    else:
        form = PollForm()
    context = {'form' : form}
    return render(request, 'polls/poll_add.html', context)


@login_required
def add_choice(request, poll_id):
    poll = get_object_or_404(Poll, id = poll_id)
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            new_choice = form.save(commit = False)
            new_choice.poll = poll
            new_choice.save()
            messages.success(request, 'Choice Added Successfully!', extra_tags = 'mt-1 alert alert-success alert-dismissible fade show')
            return HttpResponseRedirect(reverse('polls:details', args=(poll_id, )))
    else:
        form = ChoiceForm()
    return render(request, 'polls/choice_add.html', {'form' : form, 'poll' : poll})
