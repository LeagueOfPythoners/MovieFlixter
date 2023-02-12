from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_view(request, path):
    return render(request, 'index.html')
# Home page
