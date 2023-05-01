from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(requst):
    return HttpResponse('<h1>Hello from the index view in the manufacturer app</h1>')

