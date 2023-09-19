from django.urls import path
from first_app import views
urlpatterns = [
    path("", views.home, name="homepage"),
    path("about/", views.about, name="aboutpage"),
]
