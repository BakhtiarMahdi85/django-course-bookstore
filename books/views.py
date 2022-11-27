from django.shortcuts import render
from django.views import generic
from .models import Book
from django.urls import reverse_lazy

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/books_detail.html'

class CreatNewBookView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover']
    template_name = 'books/create_newbook.html'
    # form_class = UserCreationForm
    # context_object_name = 'books'
    # fields = ['title', 'author', 'description', 'price']

class UpdateBookView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover']
    template_name = 'books/update_book.html'

class DeleteBooViews(generic.DeleteView):
    model = Book
    template_name = 'books/delete_book.html'
    success_url = reverse_lazy('book_list')




