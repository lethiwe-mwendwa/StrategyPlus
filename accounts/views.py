from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreateUserForm, LoginForm, OrganisationForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Membership, Organisation

@login_required(login_url='login')
def deleteOrg(request, pk):
    organisation = get_object_or_404(Organisation, pk=pk)
    
    if request.method == "POST":
        organisation.delete()
        return redirect('organisations')

    return redirect('organisations')

@login_required(login_url='login')
def organisations(request):

    my_organisations = Organisation.objects.for_user(request.user)

    return render(request, 'accounts/organisations.html', {
        'organisations': my_organisations
    })

@login_required(login_url='login')
def createOrg(request):

    form = OrganisationForm()

    if request.method == "POST":
        form = OrganisationForm(request.POST, request.FILES)

        if form.is_valid():
            organisation = form.save(commit=False)

            # system-controlled field
            organisation.owner = request.user
            organisation.save()

            return redirect('organisations')
        

    return render(request, 'accounts/createOrg.html', {
        'form': form
    })


def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login") #go to login page

    context = {'form':form}
    
    return render(request, 'accounts/register.html', context = context)


def login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'accounts/login.html', context = context)

# User logout

def logout(request):

    auth.logout(request)

    return redirect("login")