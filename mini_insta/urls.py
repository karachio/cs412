# File: urls.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 5/26/2026
# Description: The url mapping to specific views needed for the mini insta

from django.urls import path
from .views import ProfileListView, ProfileDetailView, PostDetailView, CreatePostView, UpdateProfileView
 
 
urlpatterns = [
    path('', ProfileListView.as_view(), name="show_all_profiles"), #default
    path('show_all', ProfileListView.as_view(), name="show_all_profiles"), # modified
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='show_profile'),# new
    path('post/<int:pk>', PostDetailView.as_view(), name='show_post'),
    path('profile/<int:pk>/create_post', CreatePostView.as_view(), name='create_post'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
]
 