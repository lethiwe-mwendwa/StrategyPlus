from django.urls import path
from . import views

urlpatterns = [

        path('login', views.login, name="login"),
        path('register', views.register, name="register"),
        path('logout', views.logout, name="logout"),
        path('createOrg', views.createOrg, name="createOrg"),
        path('organisations', views.organisations, name="organisations"),
        path('organisations/delete/<int:pk>/', views.deleteOrg, name='deleteOrg'),

]
