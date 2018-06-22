from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    context={}
    lunbo=models.LunBo.objects.all()
    context['lunbo']=lunbo
    return render(request,'index.html',context=context)