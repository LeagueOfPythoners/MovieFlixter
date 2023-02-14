from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>We"re in about</h1>')

def upcoming(request):
    return render(request, 'upcoming.html')

def top10(request):
    return render(request, 'top10.html')