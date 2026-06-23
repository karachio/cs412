# File: views.py
# Author: Karachi Onwuanibe (karachio@bu.edu), 06/16/2026
# Description: the views python files that contain the form views for my project


from django.db.models import Avg, Count
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse, reverse_lazy
from .models import Project, Review, Yarn, Favorite
from django.db.models import Q

# for the class projectlistview to show list of projects
class ProjectListView(ListView):
    model = Project
    template_name = 'crochet/project_list.html'
    context_object_name = 'projects'
    
    def get_queryset(self):
        queryset = Project.objects.annotate(favorite_count=Count('favorite', distinct=True))

        category = self.request.GET.get('category', '')
        rating = self.request.GET.get('rating', '')
        difficulty = self.request.GET.get('difficulty', '')

        if category:
            queryset = queryset.filter(category__icontains=category)
        if rating:
            queryset = queryset.filter(rating=rating)
        if difficulty:
            queryset = queryset.filter(difficulty_level=difficulty)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_category'] = self.request.GET.get('category', '')
        context['selected_rating'] = self.request.GET.get('rating', '')
        context['selected_difficulty'] = self.request.GET.get('difficulty', '')
        context['categories'] = Project.objects.exclude(category='').values_list('category', flat=True).distinct()
        context['ratings'] = [1,2,3,4,5]
        context['difficulties'] = Project.DIFFICULTY_CHOICES

        # top 3 most popular
        context['popular_projects'] = Project.objects.annotate(
            favorite_count=Count('favorite', distinct=True),
            avg_rating=Avg('review__rating')
        ).order_by('-favorite_count', '-avg_rating')[:3]

        return context
    
    
# for the class projectdetailview to show project detail
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'crochet/project_detail.html'
    context_object_name = 'project'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(project=self.object)
        context['favorites'] = Favorite.objects.filter(project=self.object).count()
        context['avg_rating'] = Review.objects.filter(project=self.object).aggregate(Avg('rating'))['rating__avg']
        
        yarns = Yarn.objects.filter(project=self.object)
        context['yarns'] = yarns

        yarn_brands = list(yarns.values_list('brand', flat=True))
        yarn_names = list(yarns.values_list('name', flat=True))

        similar_raw = Project.objects.filter(
            Q(yarn__brand__in=yarn_brands) | Q(yarn__name__in=yarn_names)
        ).exclude(pk=self.object.pk).distinct()[:3]

        # attach matching yarn info to each similar project
        similar_projects = []
        for p in similar_raw:
            matching = Yarn.objects.filter(project=p).filter(
                Q(brand__in=yarn_brands) | Q(name__in=yarn_names)
            )
            similar_projects.append({
                'project': p,
                'matching_yarn': matching,
            })

        context['similar_projects'] = similar_projects
        return context

# for the class createprojectview to create projects
class CreateProjectView(CreateView):
    model = Project
    template_name = 'crochet/create_project.html'
    fields = ['title', 'creator', 'description', 'difficulty_level', 'image_file', 'project_status', 'category']

    def get_success_url(self):
        return reverse('project-list')


# for the class createreviewview to create reviews
class CreateReviewView(CreateView):
    model = Review
    template_name = 'crochet/create_review.html'
    fields = ['rating', 'review']

    def form_valid(self, form):
        form.instance.project = get_object_or_404(Project, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project-detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, pk=self.kwargs['pk'])
        return context


# for the class addyarnview to add a yarn
class AddYarnView(CreateView):
    model = Yarn
    template_name = 'crochet/add_yarn.html'
    fields = ['name', 'brand', 'color']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, pk=self.kwargs['pk'])
        return context

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
    

# for the class updateprojectbiew, to update a project
class UpdateProjectView(UpdateView):
    model = Project
    template_name = 'crochet/update_project.html'
    fields = ['title', 'creator', 'description', 'difficulty_level', 'image_file', 'project_status', 'category']

    def get_success_url(self):
        return reverse('project-detail', kwargs={'pk': self.kwargs['pk']})


# for the class deleteprojectview, to delete a project
class DeleteProjectView(DeleteView):
    model = Project
    template_name = 'crochet/delete_project.html'
    success_url = reverse_lazy('project-list')
    
    


# for the class searchyarnview, to search for yarn similarities
class SearchYarnView(ListView):
    model = Yarn
    template_name = 'crochet/yarn_search.html'
    context_object_name = 'yarns'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Yarn.objects.filter(
                Q(name__icontains=query) |
                Q(brand__icontains=query) |
                Q(color__icontains=query)
            )
        return Yarn.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')

        # yarn statistics
        context['total_yarns'] = Yarn.objects.count()
        context['total_brands'] = Yarn.objects.values('brand').distinct().count()
        context['most_used_brand'] = Yarn.objects.values('brand').annotate(count=Count('brand')).order_by('-count').first()
        context['most_popular_color'] = Yarn.objects.values('color').annotate(count=Count('color')).order_by('-count').first()
        context['most_yarns_project'] = Yarn.objects.values('project__title', 'project__pk').annotate(count=Count('id')).order_by('-count').first()

        return context


# for the class searchprojectview, to search for projects inspo
class SearchProjectView(ListView):
    model = Project
    template_name = 'crochet/project_search.html'
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = Project.objects.annotate(avg_rating=Avg('review__rating'))

        query = self.request.GET.get('q', '')
        rating = self.request.GET.get('rating', '')
        difficulty = self.request.GET.get('difficulty', '')
        status = self.request.GET.get('status', '')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__icontains=query)
            )
        if rating:
            queryset = queryset.filter(avg_rating=rating)
        if difficulty:
            queryset = queryset.filter(difficulty_level=difficulty)
        if status:
            queryset = queryset.filter(project_status=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['selected_rating'] = self.request.GET.get('rating', '')
        context['ratings'] = [1, 2, 3, 4, 5]
        context['difficulties'] = Project.DIFFICULTY_CHOICES
        context['statuses'] = Project.STATUS_CHOICES
        return context