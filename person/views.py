from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'person/index.html')

def info(request,person_id):
    return render(request,'person/info.html')

