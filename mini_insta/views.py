# File: views.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 5/26/2026
# Description: the views python files that contains the profilelistview and 
# profiledetailview, both needed to retrieve the profiles objects

from django.shortcuts import render
from .models import Post, Photo, Profile

# Create your views here.

from .models import Profile
from django.views.generic import ListView, DetailView
import random
 
 
class ProfileListView(ListView):
    '''Create a subclass of ListView to display all mini insta profiles.'''
 
 
    model = Profile # retrieve objects of type Profile from the database
    template_name = 'mini_insta/show_all_profiles.html'
    context_object_name = 'profiles' # how to find the data in the template file
 
 
class ProfileDetailView(DetailView):
   '''Show the details for one profile on mini insta.'''
   
   model = Profile
   template_name = 'mini_insta/show_profile.html' ## reusing same template!!
   context_object_name = 'profiles'
   
   
   

class PostDetailView(DetailView):
    '''Display one post on the profile.'''

    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"