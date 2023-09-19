from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def courses(request):
    return HttpResponse('''
                        <h1>Courses</h1>
                        <a href = "/">home</a>
                        <a href = "/contact/">contact</a>
                        <a href = "/about/">about</a>
                        <a href = "/feedback/">feedback</a>
                        ''')


def feedback(request):
    return HttpResponse('''
                        <h1>Feedback</h1>
                        <a href = "/">home</a>
                        <a href = "/courses/">courses</a>
                        <a href = "/contact/">contact</a>
                        <a href = "/about/">about</a>
                        ''')
