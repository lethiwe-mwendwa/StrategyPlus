from django.shortcuts import redirect, render, get_object_or_404

from accounts.models import Organisation
from projects.forms import createProjectForm
from .models import Project
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def deleteProject(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == "POST":
        project.delete()
        return redirect('projects')

    return redirect('projects')

@login_required(login_url='login')
def projectDetail(request, pk):

    project = get_object_or_404(Project, pk=pk)

    return render(request, 'projects/projectDetail.html', {'project' : project})


@login_required(login_url='login')
def dashboard(request):
    orgs = Organisation.objects.filter(membership__user=request.user)

    project_count = Project.objects.filter(
        organisation__in=orgs
    ).count()

    return render(request, 'projects/dashboard.html', {
        'projectCount': project_count,
        'organisations': orgs
    })


@login_required(login_url='login')
def projects(request):

    #learn more about this part. Refactor later btw
    my_projects = Project.objects.filter(
        organisation__membership__user=request.user
    )

    return render(request, 'projects/projects.html', {
        'projects': my_projects
    })

@login_required(login_url='login')
def createProject(request):

    if request.method == "POST":
        form = createProjectForm(request.POST)

        form.fields['organisation'].queryset = Organisation.objects.filter(
            membership__user=request.user
        )

        if form.is_valid():
            form.save()
            return redirect('projects')

    else:
        form = createProjectForm()

        form.fields['organisation'].queryset = Organisation.objects.filter(
            membership__user=request.user
        )

    return render(request, 'projects/createProject.html', {
        'form': form
    })