# File: admin.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 05/26/2026
# Description: The registration of my mini_insta

from django.contrib import admin

# Register your models here.


from .models import Profile, Post, Photo, Follow, Comment, Like
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Like)
