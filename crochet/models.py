# File: models.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 06/16/2026
# Description: the model file that contains my project models and its attributes


from django.db import models

# Create your models here.

class Project(models.Model):
    '''Encapsulate the idea of an Project by some creator.'''
 
 
    # data attributes of a Project:
    title = models.TextField(blank=False)
    creator = models.TextField(blank=False)
    description = models.TextField(blank=False)
    difficulty_level = models.TextField(blank=False)
    # image_url = models.URLField(blank=True) ## new
    image_file = models.ImageField(blank=True) # so the user can upload an image of their progress
    project_status = models.TextField(blank=False)
    category = models.TextField(blank=True, default='')
    date_created = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        '''Return a string representation of this Project object.'''
        return f'{self.title} by {self.creator}'
    
    
class Comment(models.Model):
    '''Encapsulate the idea of an Comment by some commentor.'''
    
    
    # data attributes of a Comment:
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    commenter = models.TextField(blank=False)
    comment = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this Comment object.'''
        return f'{self.commenter}: {self.comment}'
    
    
    
class Favorite(models.Model):
    '''Encapsulate the idea of an Favorite by some favoriter.'''
    
    # data attributes of a Favorite:
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    favoriter = models.TextField(blank=False)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        '''Return a string representation of this Favorite object.'''
        return f'{self.favoriter} favorited {self.project.title}'
    
    
    
class Yarn(models.Model):
    '''Encapsulate the idea of an Yarn by some project.'''
    
    # data attributes of a Yarn:
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.TextField(blank=False)
    brand = models.TextField(blank=False)
    color = models.TextField(blank=False)
    
    def __str__(self):
        '''Return a string representation of this Yarn object.'''
        return f'{self.name} by {self.brand}, ({self.color})'