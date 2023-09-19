from django.urls import include, path
from . import views
urlpatterns = [
    path("", views.home, name="home page"),
    path("show_data/", views.show_data, name="show_data")

]
