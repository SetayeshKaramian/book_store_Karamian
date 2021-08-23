from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

from book.models import Book
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Order, OrderBook
from discounts.models import Coupon


@login_required
class CartView(LoginRequiredMixin, ListView):
    def get(self, *args, **kwargs):
        return Order.objects.get(user=self.request.user, ordered=False)

    context_object_name = "order_list"
    template_name = "cart"


class OrderSummaryView(DetailView):
    model = Order
    template_name = "order_summary.html"


def check_storage(book, quantity):
    if book.storage < quantity:
        validation = False
    else:
        validation = True
    return validation


@login_required
def add_to_cart(request, pk):
    book = get_object_or_404(Book, pk=pk)
    order_qs = Order.objects.filter(user=request.user, paid=False)
    if order_qs.exists():
        order = order_qs[0]
        if OrderBook.objects.filter(book=book, order=order).exists():
            order_book = OrderBook.objects.get(book=book, order=order)
            order_book.quantity += 1
            if check_storage(book, order_book) is True:
                order_book.save()
            else:
                messages.erro(request, "not enough book in storage!")

        else:
            if check_storage(book, 1) is True:
                OrderBook.objects.create(book=book, order=order)

            else:
                messages.erro(request, "not enough book in storage!")
    else:
        if check_storage(book, 1) is True:
            order = Order.objects.create(user=request.user)
            OrderBook.objects.create(book=book, order=order)
        else:
            messages.erro(request, "not enough book in storage!")

    messages.success(request, "Cart updated!")
    return redirect("home")


@login_required
def remove_from_cart(request, pk):
    book = get_object_or_404(Book, pk=pk)
    order_qs = Order.objects.filter(user=request.user, paid=False)
    if order_qs.exists():
        order = order_qs[0]
        order_book = OrderBook.objects.filter(book=book, order=order)
        if order_book.exists():
            order_book.delete()
            messages.success(request, 'book removed from cart!')
        else:
            messages.error(request, 'there is no such a book!')
    else:
        messages.error(request, 'there is no order')
    return redirect("home")


def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(request, "This coupon does not exist")
        return redirect("home")
