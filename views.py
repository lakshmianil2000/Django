
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("hello world")

def  order(request):
    return HttpResponse("This is order page")
def about(request):
    return HttpResponse("This is about page")

# Create your views here.
