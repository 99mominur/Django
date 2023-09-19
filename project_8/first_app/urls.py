from django.urls import path
from first_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('profile/', views.profile, name='profile'),
    path('signout/', views.signout, name='logout'),
    path('passchange/', views.passchange, name='passchange'),
    path('passchange2/', views.passchange2, name='passchange2'),
]
