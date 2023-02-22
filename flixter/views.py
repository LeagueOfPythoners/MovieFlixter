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
    
    url = 'https://flixster.p.rapidapi.com/movies/get-upcoming'
    querystring = {"countryId": "usa", "limit":"100"}
    response = requests.request("GET", url, headers=headers).json()


    movies = response['data']['upcoming']
    for i in movies:
        name_m = i['name']
        image_url = i['posterImage']['url']
        release_date = i['releaseDate']
        emsId_m = i['emsVersionId']
        try:

            m = models.Upcoming.objects.get(name= name_m, image=image_url, emsId = emsId_m, date= release_date)
        except models.Upcoming.DoesNotExist:
            m = models.Upcoming.objects.create(name= name_m, image=image_url, emsId = emsId_m, date= release_date)
            m.save()
    
            
    all_movies = models.Upcoming.objects.all().values("name", "image", "date")
    posts= {'posts': all_movies}
    return render(request, 'upcoming.html', posts)

def top10(request):
    #get top 10 via reuqest limit popularity to 10
    url = "https://flixster.p.rapidapi.com/movies/get-popularity"

    response = requests.request("GET", url, headers=headers).json()


    movies = response['data']['popularity']
    for i in movies:
        if i['sortPopularity'] <11:
            name_m = i['name']
            image_url = i['posterImage']['url']
            rating_m = i['tomatoRating']['tomatometer']
            emsId_m = i['emsVersionId']

            try:
                m = models.TopTen.objects.get(name= name_m, image=image_url, emsId = emsId_m, rating= rating_m)
            except models.TopTen.DoesNotExist:
                m = models.TopTen.objects.create(name= name_m, image=image_url, emsId = emsId_m, rating= rating_m)
                m.save()
            
            
            
    all_movies = models.TopTen.objects.all().values("name", "image", "rating", 'emsId')
    posts= {'posts': all_movies}
    return render(request, 'top10.html', posts)

def one_movie(request, emsId):

    url = "https://flixster.p.rapidapi.com/movies/detail"

    querystring = {"emsVersionId": emsId }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    single_movie = response['data']['movie']

    name_m = single_movie['name']
    description_m = single_movie['synopsis']
    date_m = single_movie['releaseDate']
    image_m = single_movie['posterImage']['url']
    tags_m = single_movie['genres'][0]['name']
    rating_m = single_movie['tomatoRating']['tomatometer']

    try:
        models.Movie.objects.get(name=name_m, description = description_m, rating= rating_m,
                                 tags = tags_m, date = date_m, image = image_m )
        
    except models.Movie.DoesNotExist:
        m =  models.Movie.objects.get(name=name_m, description = description_m, rating= rating_m,
                                 tags = tags_m, date = date_m, image = image_m )
        m.save()
        
    content = models.Movie.objects.get(name= name_m, description= description_m)
    movie = {'posts':content}
    return render(request, 'singlemovie.html', movie)