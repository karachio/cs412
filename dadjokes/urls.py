# File: urls.py
# Author: Karachi Onwuanibe (karachio@bu.edu), june 11 2026
# Description: The url mapping to specific views needed for jokes


from django.urls import path
from .views import *

urlpatterns = [
    path('', RandomView.as_view(), name='home'),
    path('random/', RandomView.as_view(), name='random'),
    path('jokes/', JokeListView.as_view(), name='jokes'),
    path('joke/<int:pk>/', JokeDetailView.as_view(), name='joke'),
    path('pictures/', PictureListView.as_view(), name='pictures'),
    path('picture/<int:pk>/', PictureDetailView.as_view(), name='picture'),
    
    path(r'api/jokes/', JokeListAPIView.as_view()),
    path(r'api/jokes/<int:pk>/', JokeDetailAPIView.as_view()),
    path(r'api/pictures/', PictureListAPIView.as_view()),
    path(r'api/pictures/<int:pk>/', PictureDetailAPIView.as_view()),
    path(r'api/', RandomJokeAPIView.as_view()),
    path(r'api/random/', RandomJokeAPIView.as_view()),
    path(r'api/random_picture/', RandomPictureAPIView.as_view()),
]

