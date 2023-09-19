from django.urls import path
from second_app import views

urlpatterns = [
    path("courses/", views.courses),
    path("feedback/", views.feedback),
]