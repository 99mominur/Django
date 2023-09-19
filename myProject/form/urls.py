from django.urls import path
from . import views
urlpatterns = [
    path("", views.form, name="formpage"),
    path("djangoForm/", views.djangoForm, name="djangoForm"),
    path("studentForm/", views.passwordvalidation, name="studentForm"),
]
