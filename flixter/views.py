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

def get_movies(request):
    all_movies = {}
    if 'name' in request.GET:
        name = request.GET['name']
        url = 'https://flixster.p.rapidapi.com/movies/get-upcoming' % name
        querystring = {"countryId": "usa", "limit":"100"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        movies = data['movies']

        for i in movies:
            movie_data = Movie(
                name = i['name'],
                image = i['posterImage']['url'],
                description = i['synopsis'],
                tags = i['genres'][0]['name'],
                rating = i['tomatoRating'],
                movie_id = i['emsVersionId'],
            )
    
            movie_data.save()
            all_movies = Movie.objects.all().order_by('-id')

    return render (request, 'movie.html', {"all_movies": 
    all_movies} )
    

# @register.filter
# def get_item(dictionary, key):
#     return dictionary.get(key)

# headers = {
# 	"X-RapidAPI-Key": os.getenv("API_KEY"),
# 	"X-RapidAPI-Host": os.getenv("API_HOST") 
#     }
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html' )

def top10(request):
    return render(request, 'top10.html')

# def get_movies(request):
    
#     url = 'https://flixster.p.rapidapi.com/movies/get-upcoming'
#     querystring = {"countryId": "usa", "limit":"100"}
#     response = requests.request("GET", url, headers=headers, params=querystring).json()


#     movies = response['data']['upcoming']
#     for i in movies:
#         name_m = i['name']
#         image_url = i['posterImage']['url']
#         release_date = i['releaseDate']
#         emsId_m = i['emsVersionId']
#         try:

#             m = Movie.objects.get(name= name_m, image=image_url, emsId = emsId_m, date= release_date)
#         except Movie.DoesNotExist:
#             m = Movie.objects.create(name= name_m, image=image_url, emsId = emsId_m, date= release_date)
#             m.save()
    
            
#     all_movies = Movie.objects.all().values("name", "image", "date", "emsId")
#     posts= {'posts': all_movies}
#     return render(request, 'upcoming.html', posts)









# def top10(request):
#     #get top 10 via reuqest limit popularity to 10
#     url = "https://flixster.p.rapidapi.com/movies/get-popularity"

#     response = requests.request("GET", url, headers=headers).json()
#     print(response)


#     movies = response['data']['popularity']
#     for i in movies:
#         if i['sortPopularity'] <11:
#             name_m = i['name']
#             image_url = i['posterImage']['url']
#             rating_m = i['tomatoRating']['tomatometer']
#             emsId_m = i['emsVersionId']

#             try:
#                 m = models.TopTen.objects.get(name= name_m, image=image_url, emsId = emsId_m, rating= rating_m)
#             except models.TopTen.DoesNotExist:
#                 m = models.TopTen.objects.create(name= name_m, image=image_url, emsId = emsId_m, rating= rating_m)
#                 m.save()
            
            
            
#     all_movies = models.TopTen.objects.all().values("name", "image", "rating", 'emsId')
#     posts= {'posts': all_movies}
#     return render(request, 'top10.html', posts)

# def one_movie(request, emsId):
#     print('one_movie function')
#     url = "https://flixster.p.rapidapi.com/movies/detail"

#     querystring = {"emsVersionId": emsId }

#     response = requests.request("GET", url, headers=headers, params=querystring).json()
#     single_movie = response['data']['movie']
#     print(single_movie['name'])
#     name_m = single_movie['name']
#     description_m = ''
#     try:
#         description_m = single_movie['synopsis']
#     except: 
#         description_m = "No sypnosis assigned yet."

#     date_m = ''
#     try:
#         date_m = single_movie['releaseDate']
#     except:
#         date_m = 'None'
#     image_m =''
#    # print(single_movie['posterImage']['url']==None)
#     try:
#         image_m = single_movie['posterImage']['url']

#     except:
#         image_m = 'https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg'

#     tags_m = ''

#     try:
#         tags_m = single_movie['genres'][0]['name']
#     except: tags_m = 'No Genre Assigned'

    

#     try:
#         models.Movie.objects.get(name=name_m, description = description_m,
#                                  tags = tags_m, date = date_m, image = image_m )
        
#     except models.Movie.DoesNotExist:
#         models.Movie.objects.update_or_create(name=name_m, description = description_m, 
#                                  tags = tags_m, date = date_m, image = image_m )
        
         
#     content = models.Movie.objects.get(name= name_m, description=description_m)
#     post = {'post':content}
#     return render(request, 'singlemovie.html', post)

# def search(request):
#     print('search function')
#     url = "https://flixster.p.rapidapi.com/search"
#     if request.method != "POST":
#         return render(request, 'search.html', {})
#     else:
#         searched = request.POST.get('searched')
#         querystring = {"query":searched}
#         response = requests.request("GET", url, headers=headers, params=querystring).json()
#         data = response['data']['search']['movies']

#         m_name= ''
#         m_image = ''
#         m_emsId = ''

#         for i in data:
#         #get name
#             m_name = i['name']
#         #get image
#             #m_image = i['posterImage']['url']
#         #get emsId version
#             m_emsId = i['emsVersionId']
#             if m_image == None:
#                 try:
#                     models.Movie.objects.get(name=m_name, emsId = m_emsId )
        
#                 except models.Movie.DoesNotExist:
#                     m = models.Movie.objects.create(name=m_name, emsId = m_emsId )

#                     m.save()
#             else:
#     #create the movie or get the movie
#                 try:
#                     models.Movie.objects.get(name=m_name, emsId = m_emsId, image = m_image )
        
#                 except models.Movie.DoesNotExist:
#                     m = models.Movie.objects.create(name=m_name, emsId = m_emsId, image = m_image )

#                     m.save()

#         content = models.Movie.objects.filter(name__contains=searched).values("name", "emsId", "image")
        
#         return render(request,'search.html', {'searched':searched,
#                 'content':content} )




    



