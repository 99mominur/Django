from django.urls import path
from first_app import views
urlpatterns = [
    path("", views.home, name="homepage"),
    path("delete/<int:roll>", views.delete, name="delete_student"),
]
