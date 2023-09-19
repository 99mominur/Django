from django.shortcuts import render, redirect
from first_app.forms import RegisterForm, DataChangeForm
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.


def home(request):
    return render(request, "home.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['username']
            user_pass= form.cleaned_data['password1']
            user = authenticate(username=name, password=user_pass)
            if user is not None:
                login(request, user)
                return render(request, "profile.html", {"form": user})
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass= form.cleaned_data['password']
            user = authenticate(username=name, password=user_pass)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form":form})


def profile(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = DataChangeForm(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            return render(request, "profile.html", {"form": form})
    else:
        form = DataChangeForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

def signout(request):
    logout(request)
    return redirect("home")

def passchange(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'passchange.html', {"form":form})

def passchange2(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect("profile")
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'passchange.html', {"form":form})