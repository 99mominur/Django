from django.urls import path
from .views import home, signup,user_login, profile, user_logout, pass_change
urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("user_login/", user_login, name="user_login"),
    path("user_logout/", user_logout, name="user_logout"),
    path("profile/", profile, name="profile"),
    path("pass_change/", pass_change, name="passchange"),
]
