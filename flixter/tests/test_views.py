from django.test import TestCase
from django.urls import reverse

from flixter.models import Movie, Upcoming, TopTen

class UpcomingListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        num_of_movies = 3

        for movie in range(num_of_movies):
            Upcoming.objects.create(
                name=f'Movie Number {movie}',
                date=f'May {movie} , 2022',
                movie_id = f'wkbfgb244kj4{movie}'
            )



