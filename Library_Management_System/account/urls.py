from django.urls import path
from account import views
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("user_login/", views.user_login, name="user_login"),
    path("user_logout/", views.user_logout, name="user_logout"),
    path("profile/", views.profile, name="profile"),
    path("pass_change/", views.pass_change, name="passchange"),
    path("users/", views.users, name="users")
]