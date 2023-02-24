"""movieflixter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 

#import views
from . import views

urlpatterns = [
    path('home', views.home, name= 'flixter-home'),
    path('about', views.about, name = 'flixter-about' ),
    #add the rest of the paths
    path('upcoming', views.upcoming, name= "flixter-upcoming"),
    path('top10', views.top10, name= "flixter-top10"),
    # path('search', views.search, name= 'flixter-search'),
    # path('<str:emsId>', views.one_movie, name = "single-movie"),
    path('', views.get_movies, name = "get_movies"),
    # path('<str:movie_id> ,views.movie_description, name = "movie_description")

]
