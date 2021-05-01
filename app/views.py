from app.models import *
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'teacher.html')

def student(request):
    if request.method=="POST":
        return HttpResponse(request.POST["chosenoption"])
    return render(request,'student.html')

def startdn(request):
    trigger=Trigger(name=request.POST["course"])
    trigger.save()
    return HttpResponse(request.POST["course"])

def stopdn(request):
    trigger=Trigger.objects.get(name=request.POST["course"])
    trigger.delete()
    return HttpResponse(request.POST["course"])
