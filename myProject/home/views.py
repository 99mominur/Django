from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "./files/index.html", context= {"Author" : "mominur Rahman"})

