from django.urls import path
from . import views
urlpatterns = [
    # path("", home, name="homepage"),
    path("", views.MyTemplateView.as_view()),
    # path("store_book/", views.store_book, name="store_book_page"),
    path("store_book/", views.BookFormView.as_view(), name="store_book_page"),
    # path("show_book/", views.show_book, name="show_book_page"),
    path("show_book/", views.BookListView.as_view(), name="show_book_page"),
    path("book_details/<int:id>", views.BookdetailsView.as_view(), name="book_details"),
    # path("edit_book/<int:id>", views.edit_book, name="edit_book"),
    path("edit_book/<int:pk>", views.BookUpdateView.as_view(), name="edit_book"),
    # path("delete_book/<int:id>", views.delete_book, name="delete_book"),
    path("delete_book/<int:pk>", views.DeleteBookView.as_view(), name="delete_book"),
]
