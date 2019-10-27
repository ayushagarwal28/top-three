from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Poll, Choice, Vote
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import PollForm, ChoiceForm
import datetime
from django.db.models import Count
# Create your views here.


def poll_list(request):
    polls = Poll.objects.all();

    if 'sort-a-z' in request.GET:
        print("This is from sort-a-z")
        polls = polls.order_by('text')

    if 'date' in request.GET:
        print("This is from date")
        polls = polls.order_by('-pub_date')

    if 'votes' in request.GET:
        polls = polls.annotate(Count('vote')).order_by('-vote__count')


    paginator = paginator = Paginator(polls, 5)
    page = request.GET.get('page')
    polls = paginator.get_page(page)

    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()

    context = {'polls' : polls, 'params': params}
    return render(request, 'polls/poll_list.html', context)

@login_required
def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id = poll_id)
    user_can_vote = poll.user_can_vote(request.user)

    context = {'poll' : poll}
    if user_can_vote:
        return render(request, 'polls/poll_detail.html', context)
    else:
        results = poll.get_results_dict()
        return render(request, 'polls/poll_result.html', {'poll' : poll, 'results' : results})

@login_required
def poll_vote(request, poll_id):
    choice_id = request.POST.get('choice')
    poll = get_object_or_404(Poll, id = poll_id)
    user_can_vote = poll.user_can_vote(request.user)
    if choice_id:
        if user_can_vote:
            choice = Choice.objects.get(id = choice_id)
            new_vote = Vote(user = request.user, poll = poll, choice = choice)
            new_vote.save()
        messages.success(request, 'Your vote has been recorded!', extra_tags = 'mt-1 alert alert-success alert-dismissible fade show')
        results = poll.get_results_dict()
        return render(request, 'polls/poll_result.html', {'poll' : poll, 'results' : results})
    else:
        messages.error(request, 'Please caste your vote!', extra_tags = 'mt-1 alert alert-danger alert-dismissible fade show')
        return HttpResponseRedirect(reverse('polls:details', args=(poll_id, )))

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
            new_choice3 = Choice(
                                poll = new_poll,
                                choice_text = form.cleaned_data['choice2']
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
