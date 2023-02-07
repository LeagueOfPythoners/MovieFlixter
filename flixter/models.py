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
    
    data_created = models.DateTimeField(auto_now_add=True)
    #creation date is automatically set
    
    
    