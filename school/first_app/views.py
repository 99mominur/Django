from django.shortcuts import render, redirect
from first_app.forms import StudentForm
from .models import Student, Teacher
# Create your views here.


def home(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, "first_app/index.html", {"form": form})


def show_data(request):
    # teacher = Teacher.objects.get(name="karim")
    # students = teacher.student.all()
    # for student in students:
    #     print(student)
    students = Student.objects.get(name="Rahim")
    teachers = students.teachers.all()
    for teacher in teachers:
        print(teacher.name)
    return render(request, "first_app/index.html")
