from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from app_projects import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('app_blog.urls')),
    path('projects/', include('app_projects.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)