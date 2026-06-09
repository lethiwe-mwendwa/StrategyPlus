from django.urls import path
from . import views

urlpatterns = [

        path('login', views.login, name="Log In"),
        path('register', views.register, name="Register"),

]
