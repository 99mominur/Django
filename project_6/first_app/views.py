from django.shortcuts import render, redirect
from first_app import models
# Create your views here.

def home(request):
    student = models.Student.objects.all()
    # print(student)
    return render(request, "home.html", {"data" : student})
    
def delete(request, roll):
    student = models.Student.objects.get(pk=roll).delete()
    return redirect("homepage")