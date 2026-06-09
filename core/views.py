from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):

    #return HttpResponse('Hello world')

    return render(request, 'core/index.html')