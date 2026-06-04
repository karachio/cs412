# File: urls.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 5/26/2026
# Description: The url mapping to specific views needed for the mini insta

from django.urls import path
from .views import ProfileListView, ProfileDetailView, PostDetailView, CreatePostView, UpdateProfileView, DeletePostView, UpdatePostView, ShowFollowersDetailView, ShowFollowingDetailView, ShowFeedView, SearchView, ShowProfileView, LogoutConfirmationView
from django.contrib.auth import views as auth_views
 
 
urlpatterns = [
    path('', ProfileListView.as_view(), name="show_all_profiles"), #default
    path('show_all', ProfileListView.as_view(), name="show_all_profiles"), # modified
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='show_profile'),# new
    path('post/<int:pk>', PostDetailView.as_view(), name='show_post'),
    path('profile/create_post', CreatePostView.as_view(), name='create_post'),
    path('profile/update', UpdateProfileView.as_view(), name='update_profile'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/update', UpdatePostView.as_view(), name='update_post'),
    path('profile/<int:pk>/followers', ShowFollowersDetailView.as_view(), name='show_followers'),
    path('profile/<int:pk>/following', ShowFollowingDetailView.as_view(), name='show_following'),
    path('profile/feed/', ShowFeedView.as_view(), name='show_feed'),
    path('profile/search', SearchView.as_view(), name='search'),
    path('profile/', ShowProfileView.as_view(), name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='mini_insta/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='logout_confirmation'),name='logout'),
    path('logout/confirmation/',LogoutConfirmationView.as_view(),name='logout_confirmation'),
    
]
 