from django import forms
from books.models import BookStoreModel


class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        fields = ["id", "book_name", "author", "category"]
        widgets = {
            'id': forms.NumberInput(attrs={'class': 'bg-green-50 border border-green-500 text-green-900 placeholder-green-700 text-sm rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5 dark:bg-green-100 dark:border-green-400'}),
            'book_name': forms.TextInput(attrs={'class': 'bg-green-50 border border-green-500 text-green-900 placeholder-green-700 text-sm rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5 dark:bg-green-100 dark:border-green-400'}),
            'author': forms.TextInput(attrs={'class': 'bg-green-50 border border-green-500 text-green-900 placeholder-green-700 text-sm rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5 dark:bg-green-100 dark:border-green-400'}),
            'category': forms.TextInput(attrs={'class': 'bg-green-50 border border-green-300 text-green-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            
        }