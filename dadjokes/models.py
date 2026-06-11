from django.db import models

# Create your models here.

from django.urls import reverse
from django.contrib.auth.models import User
 
class Joke(models.Model):
    '''Encapsulate the idea of a Article by some author.'''
 
 
    # data attributes of a Joke:
    timestamp = models.DateTimeField(auto_now=True)
    contributor = models.TextField(blank=False)
    text = models.TextField(blank=False)
    
    def __str__(self):
        '''Return a string representation of this Joke object.'''
        return f'{self.text} by {self.contributor}'
    
class Picture(models.Model):
    '''Encapsulate the idea of a Article by some author.'''
 
    # data attributes of a Picture:
    image_url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    contributor = models.TextField(blank=False)
    
    def __str__(self):
        '''Return a string representation of this Joke object.'''
        return f'{self.image_url} by {self.contributor}'