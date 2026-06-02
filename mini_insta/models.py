# File: models.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 05/26/2026
# Description: The creation of my mini_insta begins here as I state out my attributes

from django.db import models
from django.urls import reverse

# Create your models here.

 
 
class Profile(models.Model):
    '''Encapsulate the idea of a Profile of a user on instagram.'''
 
 
    # data attributes of Profile needed for the user profile on mini_insta:
    username = models.TextField(blank=False)
    display_name = models.TextField(blank=False)
    bio_text = models.TextField(blank=False)
    join_date = models.DateTimeField(auto_now=True)
    profile_image_url = models.URLField(blank=True)
    
    #function to return string representation
    def __str__(self):
        '''Return a string representation of the Profile object.'''
        return f'{self.username} by {self.display_name}'
    
    def get_all_posts(self):
        '''Return all of the posts about the profile.'''
 
 
        posts = Post.objects.filter(profile=self)
        return posts
    
    def get_absolute_url(self):
        return reverse('show_profile', kwargs={'pk': self.pk})
    
    
class Post(models.Model):
    '''Encapsulate the idea of a post on an Profile on mini insta.'''

    # data attributes of a Post:
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    caption = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this Post object.'''
        return f'Post by {self.profile} on {self.timestamp}'
    
    def get_all_photos(self):
        '''Return all of the photos of a post.'''
 
 
        return self.photo_set.all()
    
    
class Photo(models.Model):
    '''Encapsulate the idea of a post on a photo on mini insta.'''

    # data attributes of a photo of the post on mini insta:
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    image_file = models.ImageField(blank=True)

    def __str__(self):
        '''Return a string representation of this Photo object.'''
        if self.image_url:
            return f'Image at {self.image_url} on {self.timestamp}'
        elif self.image_file:
            return f'Image at {self.image_file} on {self.timestamp}'
    
    def get_image_url(self):
        '''Return all of the images '''
 
        if self.image_url:
            return self.image_url
        elif self.image_file:
            return self.image_file.url
 
