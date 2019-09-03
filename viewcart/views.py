from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.views.generic.base import TemplateView
from rest_framework.response import Response
from django.shortcuts import render
import urllib
import json
import time

def dashboard(request):
    template_name = 'dashboard/dashboard.html'
    return render(request, template_name)
