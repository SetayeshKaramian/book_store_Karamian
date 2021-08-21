from book.models import Book
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderBook



@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    order_book = OrderBook.objects.create(book=book)
    order_qs = Order.objects.filter(user=request.user, paid=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(book__id=book.id).exist():
            order_book.quantity += 1
            order_book.save()
    else:
        order = Order.objects.create(user=request.user)
        order.book.add(order_book)

    messages.success(request, "Cart updated!")
    return redirect("cart")
