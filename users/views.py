from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from users.models import User
from django.http import HttpResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        user = authenticate(username=username, password=password)
    except Exception as e:
        messages.error(request, 'Wrong username/password')
        for message in messages:
            print(message.level)
        return HttpResponseRedirect('/')
    if user is not None:
        auth_login(request, user)
        request.session['username'] = username
        return HttpResponseRedirect('/dashboard')
    else:
        messages.error(request, 'Wrong username/password')
        return HttpResponseRedirect('/')


def login(request):
    template_name = 'users/login.html'
    if request.user and request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard')
    else:
        return render(request, template_name)

def logout(request):
    template_name = 'users/login.html'
    if request.user.is_authenticated:
        try:
            auth_logout(request)
            return HttpResponseRedirect('/')
        except:
            pass
    return render(request, template_name)
