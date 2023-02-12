from django.utils import timezone
from django.db import models

# Create your models here.

CHARS_MAX_LENGTH: int = 150
class Movie(models.Model):
    # movie model class (creates a table named model into our database)
    
    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    #adds column named name into movie table with no more than 150 characters
    
    description = models.TextField(blank=True, null=True)
    # movie can be created without specifying a value for the description
    
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    watch_count = models.IntegerField(default=0)
    file = models.FileField(upload_to='movies/')
    preview_image = models.ImageField(upload_to='preview_images/')
    data_created = models.DateTimeField(auto_now_add=True)
    #creation date is automatically set
    
    def __str__(self):
        return f"{self.name}, {self.description}, {self.categories}, {self.watch_count}, {self.preview_image}"

class Upcoming(models.Model):
    # movie model class (creates a table named model into our database)
    
    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    #adds column named name into movie table with no more than 150 characters
    
    description = models.TextField(blank=True, null=True)
    # movie can be created without specifying a value for the description
    
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    file = models.FileField(upload_to='movies/')
    preview_image = models.ImageField(upload_to='preview_images/')
    data_created = models.DateTimeField(auto_now_add=True)
    #creation date is automatically set
    
    def __str__(self):
        return f"{self.name}, {self.description}, {self.categories}, {self.preview_image}"
    
class TopTen(models.Model):
    # movie model class (creates a table named model into our database)
    
    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    #adds column named name into movie table with no more than 150 characters
    
    description = models.TextField(blank=True, null=True)
    # movie can be created without specifying a value for the description
    
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    watch_count = models.IntegerField(default=0)
    file = models.FileField(upload_to='movies/')
    preview_image = models.ImageField(upload_to='preview_images/')
    data_created = models.DateTimeField(auto_now_add=True)
    #creation date is automatically set
    
    def __str__(self):
        return f"{self.name}, {self.description}, {self.categories}, {self.watch_count}, {self.preview_image}"
class Category(models.Model):
    # category model
    
    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)
    # allows movie to only be under one category and if model is deleted all instances of it is deleted
    
    data_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}, {self.description}, {self.categories}"

class Tag(models.Model):
    #tag model
    
    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}, {self.description}"
    
    
    