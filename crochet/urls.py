# File: urls.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 06/16/2026
# Description: the urls file that contains the url patterns of the project


from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', views.CreateProjectView.as_view(), name='create-project'),
    path('project/<int:pk>/review/', views.CreateReviewView.as_view(), name='add-review'),
    path('project/<int:pk>/yarn/', views.AddYarnView.as_view(), name='add-yarn'),
    path('project/<int:pk>/favorite/', views.FavoriteProjectView.as_view(), name='favorite-project'),
    path('project/<int:pk>/update/', views.UpdateProjectView.as_view(), name='update-project'),
    path('project/<int:pk>/delete/', views.DeleteProjectView.as_view(), name='delete-project'),
    path('yarn/search/', views.SearchYarnView.as_view(), name='yarn-search'),
    path('project/search/', views.SearchProjectView.as_view(), name='project-search'),
    path('project/<int:pk>/advance/', views.AdvanceStatusView.as_view(), name='advance-status'),
    path('yarn/<int:pk>/update/', views.UpdateYarnView.as_view(), name='update-yarn'),
]