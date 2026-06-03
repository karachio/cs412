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
    
    def get_num_followers(self):
        '''Return the number of followers for this Profile.'''

        return Follow.objects.filter(profile=self).count()
    
    def get_num_following(self):
        '''Return the number of Profiles this Profile is following.'''

        return Follow.objects.filter(follower_profile=self).count()
    
    def get_following(self):
        '''Return a list of Profiles this Profile is following.'''

        follows = Follow.objects.filter(follower_profile=self)

        following = []
        for follow in follows:
            following.append(follow.profile)

        return following
    
    def get_followers(self):
        '''Return a list of Profiles who follow this Profile.'''

        follows = Follow.objects.filter(profile=self)

        followers = []
        for follow in follows:
            followers.append(follow.follower_profile)

        return followers
    
    def get_post_feed(self):
        '''Return all Posts from Profiles that this Profile follows.'''

        following = self.get_following()

        return Post.objects.filter(profile__in=following)
    
    
    
class Like(models.Model):
    '''Encapsulates the idea of a Profile liking a Post.'''

    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="likes")
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="likes")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this Like object.'''
        return f'{self.profile} liked {self.post} at {self.timestamp}'
    
    
    

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
    
    def get_absolute_url(self):
        return reverse('show_post', kwargs={'pk': self.pk})
    
    def get_likes(self):
        return Like.objects.filter(post=self)
    
    def get_all_comments(self):
        '''Return all comments on this Post.'''

        return Comment.objects.filter(post=self)
    
    def get_likes(self):
        '''Return all likes on this Post.'''

        return Like.objects.filter(post=self)
    
    
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
 



class Follow(models.Model):
    '''Encapsulate the idea of a Profile of a user on instagram.'''
 
 
    # data attributes of Follow needed for the user profile on mini_insta:
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="profile")
    follower_profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="follower_profile")
    timestamp = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        '''Return a string representation of this Follow object.'''
        return f'{self.follower_profile} follows {self.profile} on {self.timestamp}'
    
    
    
    
    
    
    
    
    
    
    
class Comment(models.Model):
    '''Encapsulate the idea of a Profile of a user on instagram.'''
 
 
    # data attributes of Follow needed for the user profile on mini_insta:
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="comments")
    timestamp = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=False)
    
    def __str__(self):
        '''Return a string representation of this Comment object.'''
        return f'Comment by {self.profile} on {self.post}: {self.text}'
    
    
    
    
