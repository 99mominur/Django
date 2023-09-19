from django.shortcuts import render
from .forms import contactForm, studentData, passwordvalidatonproject

# Create your views here.


def form(request):
    return render(request, "form/form.html")


def djangoForm(request):
    form = contactForm(request.POST, request.FILES)
    if form.is_valid():
        print(form.cleaned_data)
        # file = form.cleaned_data['file']
        # with open("form/upload/" + file.name, "wb+") as destination:
        #     for chunk in file.chunks():
        #         destination.write(chunk)
        # return render(request, "./form/djangoForm.html", {"form": form})
    form = contactForm()
    return render(request, "./form/djangoForm.html", {"form": form})


def studentForm(request):
    if request.method == "POST":
        form = studentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, "./form/djangoForm.html", {"form": form})
    form = studentData()
    return render(request, "./form/djangoForm.html", {"form": form})


def passwordvalidation(request):
    if request.method == "POST":
        form = passwordvalidatonproject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # return render(request, "./form/djangoForm.html", {"form": form})
    else:
        form = passwordvalidatonproject()
    return render(request, "./form/djangoForm.html", {"form": form})
