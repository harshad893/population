from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topic(request):
    topics=Topic.objects.all()
    return render(request,'display_topic.html',context={'ts':topics})

def display_webpage(request):
    webpages=Webpage.objects.all()
    return render(request,'display_webpage.html',context={'ws':webpages})
