from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from . import forms
from . import models

# Create your views here.

def center(request):
    return render(request, 'users/center.html')


def info(request, user_id):
    return render(request, 'users/info.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'error.html', {'message': '用户名或密码错误'})


def loginout(request):
    auth.logout(request)
    return HttpResponseRedirect('login')


def register(request):
    if request.method == 'GET':
        user_register_form = forms.UserRegisterForm()
        return render(request, 'register.html',{'user_register_form':user_register_form})
    if request.method == 'POST':
        user_register_form = forms.UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')

            user_profile=models.UserProfile()
            user_profile.user.username=username
            user_profile.user.password=make_password(password)

            user_profile.save()
            return render(request, 'success.html', {'message': '恭喜您，注册成功！'})
        else:
            return render(request,'error.html',{'message':user_register_form.errors})


def center(request):
    return render(request,'users/center.html')

def setting(request):
    return render(request,'users/setting.html')