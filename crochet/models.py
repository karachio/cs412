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
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    difficulty_level = models.CharField(max_length=10,choices=DIFFICULTY_CHOICES,default='easy')
    # image_url = models.URLField(blank=True) ## new
    image_file = models.ImageField(blank=True) # so the user can upload an image of their progress
    STATUS_CHOICES = [
    ('not_started', 'Not Started'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
]
    project_status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='not_started')
    category = models.TextField(blank=True, default='')
    date_created = models.DateTimeField(auto_now=True)
    RATING_CHOICES = [
    (1, '1 Star'),
    (2, '2 Stars'),
    (3, '3 Stars'),
    (4, '4 Stars'),
    (5, '5 Stars'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES,default=5)
    
    
    def __str__(self):
        '''Return a string representation of this Project object.'''
        return f'{self.title} by {self.creator}'
    
    def star_display(self):
        filled = "⭐" * self.rating
        empty = "☆" * (5 - self.rating)
        return filled + empty
        
    
class Review(models.Model):
    '''Encapsulate the idea of an Project by some creator.'''
    
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Project.RATING_CHOICES, default=5)
    review = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    '''Return a string representation of this Project object.'''
    def __str__(self):
        return f'{self.rating} stars - {self.review}'
    
    
    
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