# File: views.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 5/26/2026
# Description: the views python files that contains the profilelistview and 
# profiledetailview, both needed to retrieve the profiles objects

from django.shortcuts import render, redirect
from .models import Post, Photo, Profile, Follow, Like
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin ## NEW
from django.contrib.auth.forms import UserCreationForm ## NEW
from django.contrib.auth.models import User ## NEW
from django.contrib.auth import login # NEW

# Create your views here.

from .models import Profile
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View
import random
from .forms import UpdateProfileForm, CreateProfileForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.backends import ModelBackend
 
 
class ProfileListView(ListView):
    '''Create a subclass of ListView to display all mini insta profiles.'''
 
 
    model = Profile # retrieve objects of type Profile from the database
    template_name = 'mini_insta/show_all_profiles.html'
    context_object_name = 'profiles' 
 
class ProfileDetailView(DetailView):
   '''Show the details for one profile on mini insta.'''
   
   model = Profile
   template_name = 'mini_insta/show_profile.html' 
   context_object_name = 'profile'
   
   
   

class PostDetailView(DetailView):
    '''Display one post on the profile.'''

    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = self.get_object()
        user_profile = Profile.objects.get(user=self.request.user)

        context['has_liked'] = Like.objects.filter(
            post=post,
            profile=user_profile
        ).exists()

        return context
    
    
class CreatePostView(LoginRequiredMixin, CreateView):
    '''a view to create a post.'''

    model = Post
    fields = ['caption']
    template_name = "mini_insta/create_post_form.html"
    #context_object_name = "post"
    
    def get_login_url(self):
        '''return the URL required for login'''
        return reverse('login') 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = Profile.objects.get(user=self.request.user)
        context['profile'] = profile

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
        profile = Profile.objects.get(user=self.request.user)
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
    
    
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    '''A view to update an Article and save it to the database.'''
 
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"
    
    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)
    
    def form_valid(self, form):
        '''
        Handle the form submission to update a Profile object.
        '''
        print(f'UpdateProfileView: form.cleaned_data={form.cleaned_data}')
 
        #user = self.request.user
        #print(f"UpdateProfileView user={user} post.user={user}")
 
        # attach user to form instance (Article object):
        #form.instance.user = user
        
        
        return super().form_valid(form)
    
    


class DeletePostView(LoginRequiredMixin, DeleteView):
    '''A view to delete a comment and remove it from the database.'''
 
 
    template_name = "mini_insta/delete_post_form.html"
    model = Post
    context_object_name = 'post'
    
    def get_login_url(self):
        return reverse('login')
    
    
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
    
    
class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['caption']
    template_name = "mini_insta/update_post_form.html"
    
    def get_login_url(self):
        return reverse('login')
    
    
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
    
    
class ShowFeedView(LoginRequiredMixin, TemplateView):
    '''Display the feed for a Profile.'''

    model = Profile
    template_name = "mini_insta/show_feed.html"
    context_object_name = "profile"
    
    
        
    def get_login_url(self):
        return reverse('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #return Profile.objects.get(user=self.request.user)
       # print("user:")
        # print(self.request.user)
        # print("/n")
        # print("filter:")
        # p = Profile.objects.filter(user=self.request.user).first()
        # print(p)
        # print(p.pk)
        
        # profile doing the search
        context["profile"] = Profile.objects.get(user=self.request.user)
        
        return context
        
    
    
    
class SearchView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = "mini_insta/search_results.html"
    context_object_name = "profiles"

    def get_login_url(self):
        return reverse('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query = self.request.GET.get("q", "")

        # profile doing the search
        context["profile"] = Profile.objects.get(user=self.request.user)

        # search query
        context["query"] = query

        # POSTS (from get_queryset as required)
        context["posts"] = self.get_queryset()

        # PROFILES matching query
        profiles_by_username = Profile.objects.filter(username__icontains=query)
        profiles_by_display = Profile.objects.filter(display_name__icontains=query)
        profiles_by_bio = Profile.objects.filter(bio_text__icontains=query)

        context["profiles"] = (profiles_by_username | profiles_by_display | profiles_by_bio).distinct()

        return context
    
    def dispatch(self, request, *args, **kwargs):
        
        try:
            self.profile = Profile.objects.get(user=request.user)
        except:
            return render(request, "mini_insta/search.html", {"error": "Profile not found"})
        
        query = request.GET.get("q")

        if not query:
            profile = Profile.objects.get(user=self.request.user)
            return render(request, "mini_insta/search.html", {
                "profile": profile
            })
            
            


        return super().dispatch(request, *args, **kwargs)
    
    
    def get_queryset(self):
        query = self.request.GET.get("q", "")

        return Post.objects.filter(caption__icontains=query)
    
    

class ShowProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        viewed_profile = self.object  
        user_profile = Profile.objects.get(user=self.request.user)

        context['is_following'] = Follow.objects.filter(
            profile=viewed_profile,
            follower_profile=user_profile
        ).exists()

        return context
    
    

class LogoutConfirmationView(TemplateView):
    template_name = "mini_insta/logged_out.html"
    
    
    
class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = "mini_insta/create_profile_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["user_form"] = UserCreationForm()

        return context

    def form_valid(self, form):
        user_form = UserCreationForm(self.request.POST)

        if user_form.is_valid():
            user = user_form.save()

           
            login(self.request,user,backend='django.contrib.auth.backends.ModelBackend')

           
            form.instance.user = user

           
            return super().form_valid(form)

     
        return self.form_invalid(form)

    def get_success_url(self):
        return reverse('login')
    
    
class FollowProfileView(LoginRequiredMixin, View):

    def post(self, request, pk):
        user_profile = Profile.objects.get(user=request.user)
        target_profile = Profile.objects.get(pk=pk)

 
        if user_profile == target_profile:
            return redirect('show_profile', pk=pk)

        follow_relation = Follow.objects.filter(
            profile=target_profile,
            follower_profile=user_profile
        )

  
        if follow_relation.exists():
            follow_relation.delete()

        else:
            Follow.objects.create(
                profile=target_profile,
                follower_profile=user_profile
            )

        return redirect('show_profile', pk=pk)  
    
class DeleteFollowProfileView(LoginRequiredMixin, View):

    def post(self, request, pk):
        user_profile = Profile.objects.get(user=request.user)
        target_profile = Profile.objects.get(pk=pk)

        Follow.objects.filter(
            profile=target_profile,
            follower_profile=user_profile
        ).delete()

        return redirect('show_profile', pk=pk)
    
class LikePostView(LoginRequiredMixin, View):

    def post(self, request, pk):
        user_profile = Profile.objects.get(user=request.user)
        post = Post.objects.get(pk=pk)
        
        if post.profile == user_profile:
            return redirect('show_post', pk=pk)

        Like.objects.get_or_create(
            post=post,
            profile=user_profile  
        )

        return redirect('show_post', pk=pk)
    
class DeleteLikePostView(LoginRequiredMixin, View):

    def post(self, request, pk):
        user_profile = Profile.objects.get(user=request.user)
        post = Post.objects.get(pk=pk)

        Like.objects.filter(
            post=post,
            profile=user_profile   
        ).delete()

        return redirect('show_post', pk=pk)