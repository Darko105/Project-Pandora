from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request): #login user
    return HttpResponse('login')

def signUp(request): #singe-up
    return HttpResponse('signup')
