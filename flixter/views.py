from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from django.template.defaulttags import register
from . import models
# Create your views here.
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

headers = {
	"X-RapidAPI-Key": os.environ.get("API_KEY"),
	"X-RapidAPI-Host": os.environ.get("API_HOST") 
    }
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html' )

def upcoming(request):
    return render(request, 'upcoming.html')

def top10(request):
    #get top 10 via reuqest limit popularity to 10
    headers = {
	"X-RapidAPI-Key": os.getenv("API_KEY"),
	"X-RapidAPI-Host": os.environ.get("API_HOST") 
    }
    url = "https://flixster.p.rapidapi.com/movies/get-popularity"

    response = requests.request("GET", url, headers=headers).json()

    topMovies = {}

    movies = response['data']['popularity']
    for i in movies:
        if i['sortPopularity'] <11:
            name_m = i['name']
            image_url = i['posterImage']['url']
            rating_m = i['tomatoRating']['tomatometer']
            emsId_m = i['emsVersionId']
            m = models.TopTen.objects.create(name= name_m, image=image_url, emsId = emsId_m, rating= rating_m)
            m.save()
            '''topMovies.append(
                {'name':name,
                'image' :image_url,
                'rating' :rating}
             ) cannot be a list has to be a dict''' 
            
            
    i = 0
    all_movies = models.TopTen.objects.all().values("name", "image", "rating")
    posts= {'posts': all_movies}
    return render(request, 'top10.html', posts)