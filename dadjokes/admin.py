# karachi onwuanibe, june 11 2026
# admin.py -> for the admin site

from django.contrib import admin

# Register your models here.
from .models import Joke, Picture
admin.site.register(Joke)
admin.site.register(Picture)