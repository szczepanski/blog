from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'app_proj_projects/home.html', {'projects':projects})