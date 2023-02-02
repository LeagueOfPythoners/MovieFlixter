from flask import Flask, render_template
import pandas as pd
import requests

app = Flask(__name__)

#home page
@app.route('/')
def home():
    return render_template("index.html", title = 'Home')

@app.route('/top10')
def top10():

    url = "https://flixster.p.rapidapi.com/movies/get-popularity"


    headers = {
	"X-RapidAPI-Key": "60b5bc4261msh9a822a0d64206fep18f1c4jsn9f7333edb31f",
	"X-RapidAPI-Host": "flixster.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    topMovies = []
    print(response.text['data']['popularity'])
    movies = response.json()['data']['popularity']
    for i in movies:
        if i['sortPopularity'] <11:
            name = i['name']
            image_url = i['posterImage']['url']
            rating = i['tomatometer']
            topMovies.append(
                {'name':name,
                'image' :image_url,
                'rating' :rating}
             )

    return render_template('top10.html', len = len(topMovies), topMovies = topMovies)


@app.route('/upcoming')
def upcoming():
    url = "https://flixster.p.rapidapi.com/movies/get-upcoming"

    querystring = {"countryId":"usa","limit":"20"}

    headers = {
	"X-RapidAPI-Key": "60b5bc4261msh9a822a0d64206fep18f1c4jsn9f7333edb31f",
	"X-RapidAPI-Host": "flixster.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    upcomingMovies = []
    print(response.text['data']['upcoming'])
    movies = response.json()['data']['upcoming']
    for i in movies:
        name = i['name']
        image_url = i['posterImage']['url']
        rating = i['tomatoRating']['tomatometer']
        date = i['releaseDate']
        upcomingMovies.append(
                {'name':name,
                'image' :image_url,
                'rating' :rating,
                'release': date}
             )

app.run(use_reloader = True, debug = True)

