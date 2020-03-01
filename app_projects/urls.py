from django.urls import path
from . import views

app_name = 'app_projects'

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path('<int:project_id>/', views.detail, name='detail'),
]

# change int to slug for human readable urls
# path('<int:post_id>/', views.detail, name='detail')
