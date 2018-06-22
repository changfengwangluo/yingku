from django.shortcuts import render

# Create your views here.


def news_info(request,news_id):
    return render(request,'article/news_info.html')


def yingping_list(request,film_id):
    return render(request,'article/yingping_list.html')

def yingping_info(request,yingping_id):
    return render(request,'article/yingping_info.html')