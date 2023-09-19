
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    return HttpResponse('''
                        <h1>About</h1>
                        <a href = "/">home</a>
                        <a href = "/courses/">courses</a>
                        <a href = "/contact/">contact</a>
                        <a href = "/feedback/">feedback</a>
                        ''')

def contact(request):
    return HttpResponse('''
                        
                        <h1>Contact</h1>
                        <a href = "/">home</a>
                        <a href = "/courses/">courses</a>
                        <a href = "/about/">about</a>
                        <a href = "/feedback/">feedback</a>
                        ''')
