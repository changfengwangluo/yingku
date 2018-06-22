from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='film_index'),
    path('<int:film_id>', views.info),

    path('imgs', views.imgs),
    path('vedios', views.vedios),
]