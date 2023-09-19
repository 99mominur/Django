from django.urls import path
from . import views
urlpatterns = [
    path("", views.set_session, name="home"),
    path("get_cookie", views.get_cookie, name="get_cookie"),
]
