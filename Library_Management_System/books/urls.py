from django.urls import path
from . import views
urlpatterns = [
    path("store_book/", views.BookFormView.as_view(), name="store_book_page"),
    path("show_book/", views.BookListView.as_view(), name="show_book_page"),
    path("book_details/<int:id>", views.BookdetailsView.as_view(), name="book_details"),
    path("edit_book/<int:pk>", views.BookUpdateView.as_view(), name="edit_book"),
    path("delete_book/<int:pk>", views.DeleteBookView.as_view(), name="delete_book"),
]
 