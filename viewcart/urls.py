from django.conf.urls import url
from viewcart.views import *
from django.urls import path
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('dashboard/', login_required(dashboard), name='dashboard'),
]
