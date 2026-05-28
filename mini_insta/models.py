# File: models.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 05/26/2026
# Description: The creation of my mini_insta begins here as I state out my attributes

from django.db import models

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
 
 
        photos = Photo.objects.filter(post=self)
        return photos
    
    
class Photo(models.Model):
    '''Encapsulate the idea of a post on a photo on mini insta.'''

    # data attributes of a photo of the post on mini insta:
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this Photo object.'''
        return f'Post by {self.post} on {self.timestamp}'
 
