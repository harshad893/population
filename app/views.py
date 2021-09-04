from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from app.models import *
def display_topic(request):
    #topics=Topic.objects.all()
    #topics=Topic.objects.get(topic_name='cricket')
    topics=Topic.objects.filter(topic_name='cricket')
    return render(request,'display_topic.html',context={'ts':topics})

def display_webpage(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(topic_name='cricket')
    #webpages=Webpage.objects.all()[0:4:1]
    webpages=Webpage.objects.all().order_by('name')
    webpages=Webpage.objects.all().order_by('-name')
    webpages=Webpage.objects.all().order_by(Length('name'))
    webpages=Webpage.objects.all().order_by(Length('name').desc())
    webpages=Webpage.objects.exclude(topic_name='cricket')
    return render(request,'display_webpage.html',context={'ws':webpages})
