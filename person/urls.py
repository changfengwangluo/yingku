from django.urls import path
from . import views

urlpatterns = [

    path('', views.index,name='person_index'),
    path('<int:person_id>', views.info,name='person_info'),



]