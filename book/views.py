from django.views.generic import TemplateView, ListView, DetailView
from .models import Book, Category


class HomePageView(ListView):
    model = Book
    context_object_name = 'books'
    fields = ['title', 'author', 'publisher', 'category', 'price', 'image']
    template_name = 'home.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'BookDetail.html'
