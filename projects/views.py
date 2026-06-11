from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):

    return render(request, 'projects/dashboard.html')


@login_required(login_url='login')
def projects(request):

    return render(request, 'projects/projects.html')