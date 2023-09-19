from django.shortcuts import render
from . forms import ContactForm, SignupForm
# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        select = request.POST.get('select')
        return render(request, "about.html", {"name": name, "email": email, "select": select})
    return render(request, "about.html")


def form(request):
    return render(request, "form.html")


def django_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./first_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request, "django_form.html", {"form": form})

    form = ContactForm()
    return render(request, "django_form.html", {"form": form})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SignupForm()
    return render(request, "django_form.html", {"form": form})
