# File: views.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 06/16/2026
# Description: the views python files that contain the form views for my project



from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.urls import reverse
from .models import Project, Comment, Yarn, Favorite

# for the class projectlistview to show list of projects
class ProjectListView(ListView):
    model = Project
    template_name = 'crochet/project_list.html'
    context_object_name = 'projects'

# for the class projectdetailview to show project detail
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'crochet/project_detail.html'
    context_object_name = 'project'

# for the class createprojectview to create projects
class CreateProjectView(CreateView):
    model = Project
    template_name = 'crochet/create_project.html'
    fields = ['title', 'creator', 'description', 'difficulty_level', 'image_file', 'project_status']

    def get_success_url(self):
        return reverse('project-list')


# for the class createcommentview to create comments
class CreateCommentView(CreateView):
    model = Comment
    template_name = 'crochet/create_comment.html'
    fields = ['commenter', 'comment']

    def form_valid(self, form):
        form.instance.project = get_object_or_404(Project, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project-detail', kwargs={'pk': self.kwargs['pk']})


# for the class addyarnview to add a yarn
class AddYarnView(CreateView):
    model = Yarn
    template_name = 'crochet/add_yarn.html'
    fields = ['name', 'brand', 'color']

    def form_valid(self, form):
        form.instance.project = get_object_or_404(Project, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project-detail', kwargs={'pk': self.kwargs['pk']})


# for the class favoriteprojectview, to favorite a project
class FavoriteProjectView(View):
    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        Favorite.objects.create(project=project, favoriter='anonymous')
        return redirect(reverse('project-detail', kwargs={'pk': pk}))