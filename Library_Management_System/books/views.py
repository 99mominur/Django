from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from books.forms import BookStoreForm
from books.models import BookStoreModel
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse


# Create your views here.


# def home(request):
#     return render(request, "home.html")
# class MyTemplateView(TemplateView):
#     template_name = "home.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context = {"name": "Mominur", "age": 23}
#         # print(kwargs)
#         context.update(kwargs)
#         return context


# def store_book(request):
#     if request.method == 'POST':
#         book = BookStoreForm(request.POST)
#         if book.is_valid():
#             book.save()
#             return redirect("show_book_page")
#     else:
#         book = BookStoreForm()
#     return render(request, "store_book.html", {"form": book})

# class BookFormView(FormView):
#     template_name = "store_book.html"
#     form_class = BookStoreForm
#     success_url = reverse_lazy("show_book_page")

#     def form_valid(self, form):
#         print(form.cleaned_data)
#         form.save()
#         return redirect("show_book_page")

class BookFormView(CreateView):
    model = BookStoreModel
    template_name = "store_book.html"
    form_class = BookStoreForm
    success_url = reverse_lazy("show_book_page")

# def show_book(request):
#     book = BookStoreModel.objects.all()
#     return render(request, "show_book.html", {"form": book})


class BookListView(ListView):
    model = BookStoreModel
    template_name = "show_book.html"
    context_object_name = "form"

    # def get_uqeryset(self):
    #     return BookStoreModel.objects.filter(id="1")
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context = {"form": BookStoreModel.objects.all().order_by("id")}
    #     return context

    ordering = ["id"]
    def get_template_names(self):
        if self.request.user.is_superuser:
            pass


class BookdetailsView(DetailView):
    model = BookStoreModel
    template_name = "book_details.html"
    context_object_name = "item"
    pk_url_kwarg = "id"


def edit_book(request, id):
    book = BookStoreModel.objects.get(pk=id)
    form = BookStoreForm(instance=book)
    if request.method == 'POST':
        book = BookStoreForm(request.POST, instance=book)
        if book.is_valid():
            book.save()
            return redirect("show_book_page")
    return render(request, "store_book.html", {"form": form})


class BookUpdateView(UpdateView):
    model = BookStoreModel
    template_name = "store_book.html"
    form_class = BookStoreForm
    success_url = reverse_lazy("show_book_page")


# def delete_book(request, id):
#     book = BookStoreModel.objects.get(pk=id).delete()
#     return redirect('show_book_page')


class DeleteBookView(DeleteView):
    model = BookStoreModel
    template_name = "delete_confirmation.html"
    success_url = reverse_lazy("show_book_page")
