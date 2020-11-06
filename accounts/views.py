from django.http import  HttpResponse
from django.shortcuts import render



# Create your views here.


def register(request):
    template='blog/register.html'
    context={}
    return render(request,template,context)  

def login(request):
    template='blog/login.html'
    context={}
    return render(request,template,context)  

