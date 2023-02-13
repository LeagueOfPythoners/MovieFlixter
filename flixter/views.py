from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>We"re home</h1>')

def about(request):
    return HttpResponse('<h1>We"re in about</h1>')
