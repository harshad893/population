from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from django.db.models import Q
from django.http import HttpResponse
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
    webpages=Webpage.objects.filter(name__startswith='D')
    webpages=Webpage.objects.filter(name__endswith='k')
    webpages=Webpage.objects.filter(name__contains='r')
    webpages=Webpage.objects.filter(name__in=['Jennifer','Frank'])
    webpages=Webpage.objects.filter(name__regex=r'F[a-zA-Z]{4}')
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(Q(topic_name='cricket') & Q(name='Brian'))
    #webpages=Webpage.objects.filter(Q(topic_name='cricket'))
    #webpages=Webpage.objects.filter(Q(url__startswith='https') & Q(topic_name='Hockey'))
    
    return render(request,'display_webpage.html',context={'ws':webpages})

def display_access(request):
    access=Access_Records.objects.all()
    access=Access_Records.objects.filter(date='1999-06-25')
    access=Access_Records.objects.filter(date__gt='1999-06-25')
    access=Access_Records.objects.filter(date__gte='1999-06-25')
    access=Access_Records.objects.filter(date__lt='1999-06-25')
    access=Access_Records.objects.filter(date__lte='1999-06-25')
    access=Access_Records.objects.filter(date__month='4')
    access=Access_Records.objects.filter(date__year='2008')
    access=Access_Records.objects.filter(date__day='8')
    return render(request,'display_access.html',context={'ar':access})


def delete_webpage(request):
    #Webpage.objects.filter(topic_name='Hockey').delete()
    #return HttpResponse('Data is deleted successfully')
    Webpage.objects.all().delete()
    ws=Webpage.objects.all()
    return render(request,'display_webpage.html',context={'ws':ws})

def update_webpage(request):
    #Webpage.objects.filter(name='Teresa').update(url='http://Teresa.org/')
    Webpage.objects.filter(name='Teresa').update(topic_name='VolleyBall')
    Webpage.objects.filter(topic_name='Kabaddi').update(name='Manvith')
    Webpage.objects.filter(topic_name='Kabaddiii').update(name='Manvith')

    #Webpage.objects.update_or_create(name='Teresa',defaults={'url':'http://VollyBall.org/'})
    #Webpage.objects.update_or_create(name='Manvith',defaults={'url':'http://Kabaddi.org/'})
    t=Topic.objects.get_or_create(topic_name='cricket')[0]
    t.save()
    Webpage.objects.update_or_create(name='Harshad',defaults={'topic_name':t,'name':'Harshad','url':'http://VollyBall.org/'})
    ws=Webpage.objects.all()
    return render(request,'display_webpage.html',context={'ws':ws})