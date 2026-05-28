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
        fields = ['profile', 'caption', 'timestamp']
        
    