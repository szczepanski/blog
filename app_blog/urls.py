from django.urls import path
from . import views

app_name = 'app_blog'

# urlpatterns = [
#     path('', views.all_posts, name='all_posts'),
#     path('<int:post_id>/', views.detail, name='detail'),
# ]

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<slug:slug>/', views.detail, name='detail'),
]

# change int to slug for human readable urls
# path('<int:post_id>/', views.detail, name='detail')
