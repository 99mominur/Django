from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def courses(request):
    return HttpResponse(''' 
                        This is courses page
                        <a href = "/first_app/contact/">Contact</a>
                        <a href = "/first_app/about/">About</a>
                        <a href = "/second_app/feedback/">Feedback</a>
                        ''')

def feedback(request):
    return HttpResponse(''' 
                        This is feedbck page
                        <a href = "/first_app/contack/">Contact</a>
                        <a href = "/first_app/about/">About</a>
                        <a href = "/second_app/courses/">Courses</a>
                        ''')