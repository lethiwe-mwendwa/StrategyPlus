from django.urls import path
from . import views

urlpatterns = [
    
        path('dashboard', views.dashboard, name="Dashboard"),
        path('projects', views.projects, name="projects"),

]
