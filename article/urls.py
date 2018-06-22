from django.urls import path
from . import views

urlpatterns = [
    path('yingping/l<int:film_id>', views.yingping_list,name='yingping_list'),
    path('yingping/i<int:yingping_id>', views.yingping_info,name='yingping_info'),
]