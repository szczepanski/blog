from django.contrib import admin
from .models import Project

# show particular application's model in web admin gui - register it 
admin.site.register(Project)