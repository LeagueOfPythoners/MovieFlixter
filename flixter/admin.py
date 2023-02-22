from django.contrib import admin

from flixter.models import Movie
from flixter.models import Category
from flixter.models import Tag
from flixter.models import Upcoming
from flixter.models import TopTen
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "preview_image")
    #list_filter = ("categories")
#admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Upcoming)
admin.site.register(TopTen)