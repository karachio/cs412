# File: views.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 5/26/2026
# Description: the views python files that contains the profilelistview and 
# profiledetailview, both needed to retrieve the profiles objects

from django.shortcuts import render
from .models import Post, Photo, Profile
from django.urls import reverse

# Create your views here.

from .models import Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import random
from .forms import UpdateProfileForm
 
 
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
    
    
class UpdateProfileView(UpdateView):
    '''A view to update an Article and save it to the database.'''
 
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"
    
    def form_valid(self, form):
        '''
        Handle the form submission to update a Profile object.
        '''
        print(f'UpdateProfileView: form.cleaned_data={form.cleaned_data}')
 
 
        return super().form_valid(form)
    
    


class DeletePostView(DeleteView):
    '''A view to delete a comment and remove it from the database.'''
 
 
    template_name = "mini_insta/delete_post_form.html"
    model = Post
    context_object_name = 'post'
    
    def get_success_url(self):
        '''Return a the URL to which we should be directed after the delete.'''
 
 
        # get the pk for this comment
        #pk = self.kwargs.get('pk')
        post = self.object
        
        # find the article to which this Comment is related by FK
        profile = post.profile
        
        # reverse to show the article page
        return reverse('show_profile', kwargs={'pk':profile.pk})
    
    
    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''
 
 
        # calling the superclass method
        context = super().get_context_data(**kwargs)
 
 
        # find/add the post to the context data
        # retrieve the PK from the URL pattern
        #pk = self.kwargs['pk']
        posts = self.object
        profile = self.object
 
 
        # add this post into the context dictionary:
        context['posts'] = posts
        context['profile'] = profile
        return context
    
    
class UpdatePostView(UpdateView):
    model = Post
    fields = ['caption']
    template_name = "mini_insta/update_post_form.html"
    
    
class ShowFollowersDetailView(DetailView):

    model = Profile
    template_name = "mini_insta/show_followers.html"
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = self.object
        context['followers'] = profile.get_followers()

        return context
    
class ShowFollowingDetailView(DetailView):
    
    model = Profile
    template_name = "mini_insta/show_following.html"
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = self.object
        context['following'] = profile.get_following()

        return context
    
    
class ShowFeedView(DetailView):
    '''Display the feed for a Profile.'''

    model = Profile
    template_name = "mini_insta/show_feed.html"
    context_object_name = "profile"