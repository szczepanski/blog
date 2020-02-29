from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'app_proj_root/home.html', {'projects':projects})


def all_projects(request):
    counter_projects = Project.objects.count
    # order by most recent and limit to last 10 posts
    projects = Project.objects.order_by('-date')[:10]
    
    
    return render(request, 'app_proj_projects/all_projects.html', {'projects':projects, 'counter_projects': counter_projects })

def detail(request, post_id):
    post = get_object_or_404(Project, pk=project_id)
    return render(request, 'app_proj_project/detail.html',{'post':post})