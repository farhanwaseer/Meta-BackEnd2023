from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> Welcome to Little Lemon! </h1>")

def farhan(request):
    return HttpResponse("<h1> Welcome to Little Lemon! By Farhan Waseer </h1>")
