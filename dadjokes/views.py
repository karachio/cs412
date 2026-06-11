# File: views.py
# Author: Karachi Onwuanibe (karachio@bu.edu), june 11 2026
# Description: The views file for joke


from django.shortcuts import render

# Create your views here.
import random
from django.views.generic import ListView, DetailView, TemplateView
from .models import Joke, Picture

from rest_framework import generics
from .serializers import *
from .serializers import JokeSerializer, PictureSerializer
import random

class RandomView(TemplateView):
    template_name = "dadjokes/random.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['joke'] = random.choice(Joke.objects.all())
        context['picture'] = random.choice(Picture.objects.all())

        return context
    
class JokeListView(ListView):
    model = Joke
    template_name = "dadjokes/jokes.html"
    context_object_name = "jokes"
    
class JokeDetailView(DetailView):
    model = Joke
    template_name = "dadjokes/joke.html"
    context_object_name = "joke"
    
class PictureListView(ListView):
    model = Picture
    template_name = "dadjokes/pictures.html"
    context_object_name = "pictures"
    
class PictureDetailView(DetailView):
    model = Picture
    template_name = "dadjokes/picture.html"
    context_object_name = "picture"
    
    
    
class JokeListAPIView(generics.ListCreateAPIView):
    """
    List all jokes or create a new joke.
    """
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer


class JokeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single joke.
    """
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
    
class PictureListAPIView(generics.ListCreateAPIView):
    """
    List all pictures or create a new picture.
    """
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class PictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single picture.
    """
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    
class RandomJokeAPIView(generics.RetrieveAPIView):
    serializer_class = JokeSerializer

    def get_object(self):
        all_jokes = Joke.objects.all()

        n = random.randint(0, len(all_jokes) - 1)

        return all_jokes[n]
    
class RandomPictureAPIView(generics.RetrieveAPIView):
    serializer_class = PictureSerializer

    def get_object(self):
        all_pictures = Picture.objects.all()
        n = random.randint(0, len(all_pictures) - 1)
        return all_pictures[n]