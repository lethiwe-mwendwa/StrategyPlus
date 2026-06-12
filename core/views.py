from django.shortcuts import render, redirect

# from django.http import HttpResponse

def home(request):

    #if request.user.is_authenticated:
    #    return redirect('dashboard')

    #return HttpResponse('Hello world')
    return render(request, 'core/index.html')