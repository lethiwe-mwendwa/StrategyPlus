from django.urls import path
from . import views

urlpatterns = [
    
        path('dashboard', views.dashboard, name="dashboard"),
        path('projects', views.projects, name="projects"),
        path('createProject', views.createProject, name="createProject"),

        # Maps URLs like /article/1/ or /article/42/
        path('projects/<int:pk>/', views.projectDetail, name='projectDetail'),
        path('projects/delete/<int:pk>/', views.deleteProject, name='deleteProject'),


]
