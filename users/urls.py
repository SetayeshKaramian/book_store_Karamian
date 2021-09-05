from django.urls import path, re_path
from .views import *
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('profile/', userpage, name='profile'),
    path('profile_update/', UpdateProfile.as_view(), name='update_profile'),
]
