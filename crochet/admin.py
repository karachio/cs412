# File: admin.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 06/16/2026
# Description: the admin in charge of creaing project, comment, favorite and yarn



from django.contrib import admin

# Register your models here.
from .models import Project, Comment, Favorite, Yarn
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Favorite)
admin.site.register(Yarn)