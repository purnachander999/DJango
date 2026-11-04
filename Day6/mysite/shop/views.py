from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Shop Home Page")

def product(request):
    return HttpResponse("Shop products Page")
