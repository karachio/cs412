# File: models.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 05/26/2026
# Description: The creation of my mini_insta

from django.db import models

# Create your models here.

 
 
class Profile(models.Model):
    '''Encapsulate the idea of a Profile of a user on instagram.'''
 
 
    # data attributes of Profile:
    username = models.TextField(blank=False)
    display_name = models.TextField(blank=False)
    bio_text = models.TextField(blank=False)
    join_date = models.DateTimeField(auto_now=True)
    profile_image_url = models.URLField(blank=True)
    
    def __str__(self):
        '''Return a string representation of the Profile object.'''
        return f'{self.username} by {self.display_name}'
 
