# File: views.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 5/26/2026
# Description: the views python files that contains the profilelistview and 
# profiledetailview, both needed to retrieve the profiles objects

from django.shortcuts import render
from .models import Post, Photo, Profile
from django.urls import reverse

# Create your views here.

from .models import Profile
from django.views.generic import ListView, DetailView, CreateView
import random
 
 
class ProfileListView(ListView):
    '''Create a subclass of ListView to display all mini insta profiles.'''
 
 
    model = Profile # retrieve objects of type Profile from the database
    template_name = 'mini_insta/show_all_profiles.html'
    context_object_name = 'profiles' # how to find the data in the template file
 
 
class ProfileDetailView(DetailView):
   '''Show the details for one profile on mini insta.'''
   
   model = Profile
   template_name = 'mini_insta/show_profile.html' 
   context_object_name = 'profiles'
   
   
   

class PostDetailView(DetailView):
    '''Display one post on the profile.'''

    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"
    
    
class CreatePostView(CreateView):
    '''a view to create a post.'''

    model = Post
    fields = ['caption']
    template_name = "mini_insta/create_post_form.html"
    context_object_name = "post"
    
    
    def get_context_data(self):
        '''Return the dictionary of context variables for use in the template.'''
 
 
        # calling the superclass method
        context = super().get_context_data()
 
 
        # find/add the post to the context data
        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        posts = Profile.objects.get(pk=pk)
 
 
        # add this post into the context dictionary:
        context['posts'] = posts
        context['profiles'] = Profile.objects.get(pk=pk)
        return context
    
    
    
    def form_valid(self, form):
        '''This method handles the form submission and saves the 
        new object to the Django database.
        We need to add the foreign key (of the Photo) to the Post
        object before saving it to the database.
        '''
 
 
		# instrument our code to display form fields: 
        print(f"CreatePostView.form_valid: form.cleaned_data={form.cleaned_data}")
        
        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        # attach this post to the comment
        form.instance.profile = profile # set the FK
        
        response = super().form_valid(form)
 
        #image_url = self.request.POST.get('image_url')
       # if image_url:
       #     Photo.objects.create(post=self.object, image_url=image_url)
       
        images = self.request.FILES.getlist('image')
        for img in images:
            Photo.objects.create(post=self.object, image_file=img)
        
        # delegate the work to the superclass method form_valid:
        return response
    
    
    def get_success_url(self):
        return reverse('show_post', kwargs={'pk': self.object.pk})