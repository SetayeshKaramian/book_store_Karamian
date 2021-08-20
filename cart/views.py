from django.shortcuts import render, get_object_or_404
from book.models import Book
from .models import Order, OrderBook


def add_to_cart(request, slug):
    book = get_object_or_404(Book, slug=slug)
    order_book = OrderBook.objects.create(book=book)
    order_qs = Order.objects.filter(user=request.user, paid=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
