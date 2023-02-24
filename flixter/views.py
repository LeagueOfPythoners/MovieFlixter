from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from django.template.defaulttags import register
from .models import Movie, Upcoming, TopTen
# Create your views here.

headers = {
	"X-RapidAPI-Key": os.getenv("API_KEY"),
	"X-RapidAPI-Host": os.getenv("API_HOST") 
}




    

# @register.filter
# def get_item(dictionary, key):
#     return dictionary.get(key)

headers = {
 	"X-RapidAPI-Key": os.getenv("API_KEY"),
 	"X-RapidAPI-Host": os.getenv("API_HOST") 
     }
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html' )

def contact(request):
    return render(request, 'contact.html')


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
             movie_id_m = i['emsVersionId']

             try:
                 m = TopTen.objects.get(name= name_m, image=image_url, movie_id = movie_id_m, rating= rating_m)
             except TopTen.DoesNotExist:
                 m = TopTen.objects.create(name= name_m, image=image_url, movie_id = movie_id_m, rating= rating_m)
                 m.save()
            
            
            
     all_movies = TopTen.objects.all().values("name", "image", "rating", 'movie_id')
     posts= {'posts': all_movies}
     return render(request, 'top10.html', posts)

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

            m = Upcoming.objects.get(name= name_m, image=image_url, movie_id = emsId_m, date= release_date)
        except Upcoming.DoesNotExist:
            m = Upcoming.objects.create(name= name_m, image=image_url, movie_id = emsId_m, date= release_date)
            m.save()
    
            
    all_movies = Upcoming.objects.all().values("name", "image", "date", "movie_id")
    posts= {'posts': all_movies}
   
    return render(request, 'upcoming.html', posts)


def movie_description(request, movie_id):
     url = "https://flixster.p.rapidapi.com/movies/detail"

     querystring = {"emsVersionId": movie_id }

     response = requests.request("GET", url, headers=headers, params=querystring).json()
     single_movie = response['data']['movie']
     name_m = single_movie['name']

     try:
         description_m = single_movie['synopsis']
     except: 
         description_m = "No sypnosis assigned yet."

     try:
         date_m = single_movie['releaseDate']
     except:
         date_m = 'None'
    # print(single_movie['posterImage']['url']==None)
     try:
         image_m = single_movie['posterImage']['url']

     except:
         image_m = 'https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg'


     try:
         tags_m = single_movie['genres'][0]['name']

     except: 
         tags_m = 'No Genre Assigned'

    

     try:
         Movie.objects.get(name=name_m, description = description_m,
                                  tags = tags_m, date = date_m, image = image_m )
        
     except Movie.DoesNotExist:
         m =Movie.objects.create(name=name_m, description = description_m, 
                                  tags = tags_m, date = date_m, image = image_m )
         m.save()
        
         
     content = Movie.objects.get(name= name_m, description=description_m)
     movie = {'post':content}
     return render(request, 'movie_description.html', movie)

def get_movies(request):
     url = "https://flixster.p.rapidapi.com/search"
     if request.method != "POST":
         return render(request, 'movie.html', {})
     else:
         searched = request.POST.get('searched')
         querystring = {"query":searched}
         response = requests.request("GET", url, headers=headers, params=querystring).json()
         data = response['data']['search']['movies']

         m_name= ''
         m_image = ''
         m_emsId = ''

         for i in data:
         #get name
             m_name = i['name']
         #get image
             #m_image = i['posterImage']['url']
         #get emsId version
             m_emsId = i['emsVersionId']
             if m_image == None:
                 try:
                     Movie.objects.get(name=m_name, movie_id = m_emsId )
        
                 except Movie.DoesNotExist:
                     m = Movie.objects.create(name=m_name, emsId = m_emsId )

                     m.save()
             else:
     #create the movie or get the movie
                 try:
                     Movie.objects.get(name=m_name, movie_id = m_emsId, image = m_image )
        
                 except Movie.DoesNotExist:
                     m = Movie.objects.create(name=m_name, movie_id = m_emsId, image = m_image )

                     m.save()

         content = Movie.objects.filter(name__contains=searched).values("name", "movie_id", "image")
        
         return render(request,'movie.html', {'searched':searched,
                 'content':content} )




    



