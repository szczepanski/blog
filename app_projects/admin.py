from django.contrib import admin
from .models import Project

# show particular application's model in web admin gui - register it 
# admin.site.register(Project)



class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'brief',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Project, ProjectAdmin)