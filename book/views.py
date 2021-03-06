from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView
from .models import Book, Category


class HomePageView(ListView):
    queryset = Book.objects.order_by('sold')[0:10]
    context_object_name = 'books'
    fields = ['title', 'author', 'publisher', 'category', 'price', 'image']
    template_name = 'index.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'product.html'


class SearchResultListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(publisher__icontains=query)
        )
