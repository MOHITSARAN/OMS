from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.views.generic.base import TemplateView
from rest_framework.response import Response
from django.shortcuts import render
import urllib
import json
import time

def order(request):
    template_name = 'catalog/create.html'
    return render(request, template_name)

def view_order(request):
    template_name = 'catalog/view_order.html'
    return render(request, template_name)


def product(request):
    template_name = 'catalog/create_product.html'
    return render(request, template_name)

def view_product(request):
    template_name = 'catalog/view_product.html'
    return render(request, template_name)


def customer(request):
    template_name = 'catalog/create_customer.html'
    return render(request, template_name)

def view_customer(request):
    template_name = 'catalog/view_customer.html'
    return render(request, template_name)