from django.urls import path
from . import views

urlpatterns = [
    path('', views.center, name='users_center'),
    path('<int:user_id>', views.info, name='user_info'),

    path('login', views.login, name='login'),
    path('loginout', views.loginout, name='loginout'),
    path('register', views.register, name='register'),

    path('center', views.center, name='user_center'),
    path('setting', views.setting, name='person_setting'),

]
