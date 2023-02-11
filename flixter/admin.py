from django.contrib import admin

from flixter.models import Movie
from flixter.models import Category
from flixter.models import Tag
# Register your models here.

admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Tag)