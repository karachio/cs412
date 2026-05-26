from django.urls import path
from .views import ProfileListView
 
 
urlpatterns = [
    path('', ProfileListView.as_view(), name="show_all_profiles"), #default
    path('show_all', ProfileListView.as_view(), name="show_all_profiles"), # modified
    #path('article/<int:pk>', ArticleView.as_view(), name='article'),# new
]
 