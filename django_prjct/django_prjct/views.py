#from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')


def homepage(request):
    return render(request, 'homepage.html')