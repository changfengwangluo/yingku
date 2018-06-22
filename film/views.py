from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'film/index.html')

def info(request,film_id):
    return render(request,'film/info.html')

def imgs(request):
    return render(request,'film/imgs.html')

def vedios(request):
    return render(request,'film/vedios.html')

