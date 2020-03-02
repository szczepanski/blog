from django.shortcuts import render, get_object_or_404
from .models import Project
from app_blog.models import Post


def home(request):
    projects = Project.objects.all()
    posts = Post.objects.all()
    return render(request, 'app_proj_root/home.html', {'projects':projects, 'posts':posts})


def all_projects(request):
    counter_projects = Project.objects.count
    # order by most recent and limit to last 10 posts
    projects = Project.objects.order_by('-date')[:10]
    
    
    return render(request, 'app_proj_projects/all_projects.html', {'projects':projects, 'counter_projects': counter_projects })

# def detail(request, slug):
#     project = get_object_or_404(Project, pk=slug)
#     return render(request, 'app_proj_project/detail.html',{'project':project})


def detail(request, slug):
    project = get_object_or_404(Project, pk=slug)
    return render(request, 'app_proj_project/detail.html',{'project':project})