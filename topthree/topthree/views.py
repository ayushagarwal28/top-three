from django.http import HttpResponse
from django.shortcuts import render
import datetime

def curr_date_time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html" % now
    return HttpResponse(html)

def home(request):
    context = {'insert_me' : 'This is my dynamic data'}
    return render(request, 'home.html', context)
