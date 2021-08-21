from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', add_to_cart, name='cart')
]