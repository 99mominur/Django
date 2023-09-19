from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello, this is my home page</h1>")


def about(request):
    return HttpResponse("<h1>Hello, this is my about page</h1>")
