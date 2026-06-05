# File: forms.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 5/28/2026
# Description: The initialization of forms for the models

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    '''A form to add a Post to the database.'''
 
 
    class Meta:
        '''Associate this form with the Post model; select fields to add.'''
        model = Post
        fields = ['profile', 'caption']#, 'timestamp']
        
        
class UpdateProfileForm(forms.ModelForm):
    '''A form to update a profile to the database.'''
 
    class Meta:
        '''associate this form with the Article model.'''
        model = Profile
        fields = ['display_name', 'bio_text', 'profile_image_url' ]  # which fields from model should we use
    
