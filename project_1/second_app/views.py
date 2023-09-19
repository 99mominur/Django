from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    return HttpResponse("<h1>Hello, this is my contact page. </h1>")