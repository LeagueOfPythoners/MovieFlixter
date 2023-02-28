from django.test import TestCase

from flixter.models import Movie, Upcoming, TopTen 

class MovieModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Movie.objects.create(name='Test Movie', date='May 12, 2023')

    def test_name_label(self):
        author = Movie.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_date_label(self):
        author = Movie.objects.get(id=1)
        field_label = author._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

class UpcomingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Upcoming.objects.create(name='Test Movie', date='May 12, 2023')

    def test_name_label(self):
        author = Upcoming.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_date_label(self):
        author = Upcoming.objects.get(id=1)
        field_label = author._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

class TopTenModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        TopTen.objects.create(name='Test Movie', rating='89')

    def test_name_label(self):
        author = TopTen.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_date_label(self):
        author = TopTen.objects.get(id=1)
        field_label = author._meta.get_field('rating').verbose_name
        self.assertEqual(field_label, 'rating')

    

