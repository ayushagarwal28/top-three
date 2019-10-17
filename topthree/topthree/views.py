from django.http import HttpResponse
from django.shortcuts import render
import datetime

def curr_date_time(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>It is now %s.</h1></body></html" % now
    return HttpResponse(html)

def home(request):
    return render(request, 'home.html')
