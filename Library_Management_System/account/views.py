from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    return render(request, "account/home.html")


def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, message="Successfully Created User")
                # print(form.cleaned_data)
                form.save()
        else:
            form = RegisterForm()
        return render(request, "signup.html", {"form": form})
    else:
        return redirect("profile")


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data["username"]
                userpass = form.cleaned_data["password"]
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    login(request, user)
                    return redirect("profile")
        else:
            form = AuthenticationForm()
        return render(request, "signin.html", {"form": form})
    else:
        return redirect("profile")


def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(
                    request, message="Account Updated Successfully")
                # print(form.cleaned_data)
                form.save()
        else:
            form = ChangeUserData(instance=request.user)
        return render(request, "profile.html", {"form": form})
    else:
        return redirect("signup")


def user_logout(request):
    logout(request)
    return redirect("user_login")


def pass_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, "pass_change.html", {'form': form})
    else:
        return redirect("user_login")


def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(
                    request, message="Account Updated Successfully")
                # print(form.cleaned_data)
                form.save()
        else:
            form = ChangeUserData()
        return render(request, "profile.html", {"form": form})
    else:
        return redirect("signup")


def users(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            people = User.objects.all()
            return render(request, "users.html", {"users": people})
        else:
            return redirect("profile")
        
    else:
        return redirect("signup")
