from django.http import  HttpResponse
from django.shortcuts import render



# Create your views here.

def home(request):
    template='blog/home.html'
    context={}
    return render(request,template,context)

def vegitable(request):
    template='blog/vegitable.html'
    context={}
    return render(request,template,context)

def fish(request):
    template='blog/fish.html'
    context={}
    return render(request,template,context)

def meet(request):
    template='blog/meet.html'
    context={}
    return render(request,template,context)

def rice(request):
    template='blog/rice.html'
    context={}
    return render(request,template,context)    

def machine(request):
    template='blog/machine.html'
    context={}
    return render(request,template,context)    

def madichine(request):
    template='blog/madichine.html'
    context={}
    return render(request,template,context)  


def order(request):
    template='blog/order.html'
    context={}
    return render(request,template,context)  

def chart(request):
    template='blog/chart.html'
    context={}
    return render(request,template,context)  

def register(request):
    template='blog/register.html'
    context={}
    return render(request,template,context)  

def login(request):
    template='blog/login.html'
    context={}
    return render(request,template,context)  

def about(request):
    template='blog/about.html'
    context={}
    return render(request,template,context)     

def agency(request):
    template='blog/agency.html'
    context={}
    return render(request,template,context)      

def blog(request):
    template='blog/blog.html'
    context={}
    return render(request,template,context) 

def training(request):
    template='blog/training.html'
    context={}
    return render(request,template,context) 

def home(request):
    template='blog/logout.html'
    context={}
    return render(request,template,context)     