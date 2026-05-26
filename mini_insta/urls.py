from django.urls import path
from .views import ProfileListView, ProfileDetailView
 
 
urlpatterns = [
    path('', ProfileListView.as_view(), name="show_all_profiles"), #default
    path('show_all', ProfileListView.as_view(), name="show_all_profiles"), # modified
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='show_profile'),# new
]
 