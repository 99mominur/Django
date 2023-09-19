from django.shortcuts import render
from first_app.forms import StudentForm
# Create your views here.

def home(request):
    if request.method == "POST":
        student = StudentForm(request.POST)
        if student.is_valid():
            student.save()
            print(student.cleaned_data)
    else:
        student = StudentForm()
    return render(request, "home.html", {"form" : student})