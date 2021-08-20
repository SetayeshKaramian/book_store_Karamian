from django.views.generic import TemplateView, ListView
from .models import Book, Category


class HomePageView(ListView):
    model = Book
    context_object_name = 'books'
    fields = ['title', 'author']
    template_name = 'home.html'
