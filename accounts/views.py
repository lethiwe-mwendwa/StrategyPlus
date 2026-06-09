from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm

def login(request):

    return render(request, 'accounts/login.html')

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login") #go to login page

    context = {'form':form}
    
    return render(request, 'accounts/register.html', context = context)