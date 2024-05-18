from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse
def insert_topic(request):

    if request.method=='POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic inserted sucessfully')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        WO.save()
        return HttpResponse('Webpage is created')


    return render(request,'insert_webpage.html',d)



def select_multiple(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}

    if request.method=='POST':
        STL=request.POST.getlist('tn')
        print(STL)
        WOS=Webpage.objects.none()
        for t in STL:
            WOS=WOS|Webpage.objects.filter(topic_name=t)
        d1={'WOS':WOS}
        return render(request,'display_webpage.html',d1)

    return render(request,'select_multiple.html',d)





def checkbox(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}

    return render(request,'checkbox.html',d)











































