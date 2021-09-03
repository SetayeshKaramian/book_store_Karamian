from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View, FormView
from .models import Order, OrderBook
from discounts.models import Coupon
from book.models import Book
from .forms import CheckoutForm
from users.models import Address
from discounts.forms import CouponForm


def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


def check_storage(book, quantity):
    if book.storage < quantity:
        validation = False
    else:
        validation = True
    return validation


# show unpaid order
class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, paid=False)
            context = {
                'object': order
            }
            return render(self.request, 'cart/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, 'شما هیچ سفارش فعالی ندارید.')
            return redirect("/")


class CheckoutFormView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, paid=False)
            form = CheckoutForm()
            context = {
                'form': form,
                'order': order,
                'couponform': CouponForm,
            }
            shipping_address_qs = Address.objects.filter(
                user=self.request.user,
                default=True
            )
            if shipping_address_qs.exists():
                context.update(
                    {'default_shipping_address': shipping_address_qs[0]})
            return render(self.request, "cart/checkout.html", context)

        except ObjectDoesNotExist:
            messages.info(self.request, 'You do not have an active order')
            return redirect("checkout/")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, paid=False)
            if form.is_valid():
                # use_default_shipping = form.cleaned_data.get(
                #     'use_default_shipping')
                # if use_default_shipping:
                #     print("Using the defualt shipping address")
                #     address_qs = Address.objects.filter(
                #         user=self.request.user,
                #         default=True
                #     )
                #     if address_qs.exists():
                #         shipping_address = address_qs[0]
                #         order.shipping_address = shipping_address
                #         order.save()
                #     else:
                #         messages.info(
                #             self.request, "No default shipping address available")
                #         return redirect('core:checkout')
                # else:
                #     print("User is entering a new shipping address")
                #     shipping_address = form.cleaned_data.get('shipping_address')
                #     shipping_zip_code= form.cleaned_data.get('shipping_zip_code')
                #
                #     if is_valid_form([shipping_address, shipping_zip_code]):
                #         shipping_address = Address(
                #             user=self.request.user,
                #             address=shipping_address,
                #             zip_code=shipping_zip_code,
                #         )
                #     shipping_address.save()
                #     order.shipping_address = shipping_address
                #     order.save()

                billing_address = form.cleaned_data.get('billing_address')
                order.billing_address = billing_address
                order.save()

                paid = form.cleaned_data.get('paid')
                order.paid = paid
                order.save()
                return redirect('/')

        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("order-summary/")


@login_required
def add_to_cart(request, pk):
    """For adding to cart func checks if there is any active order and order_books. They will be updated
     Otherwise the algorithm will create them. Also this func checks if we have enough storage and update
     the sold filed"""

    book = get_object_or_404(Book, pk=pk)
    order_qs = Order.objects.filter(user=request.user, paid=False)
    if order_qs.exists():
        order = order_qs[0]
        if OrderBook.objects.filter(book=book, order=order).exists():
            order_book = OrderBook.objects.get(book=book, order=order)
            order_book.quantity += 1
            if check_storage(book, order_book.quantity) is True:
                # update storage, quantity and sold fields
                order_book.book.storage -= 1
                order_book.book.sold += 1
                order_book.save()
                order_book.book.save()
                messages.success(request, "کتاب با موفقیت به سبد خرید افزوده شد!")
            else:
                messages.error(request, "موجودی کتاب کافی نمی‌باشد!")
        else:
            if check_storage(book, 1) is True:
                order_book = OrderBook.objects.create(book=book, order=order)
                order_book.book.storage -= 1
                order_book.book.sold += 1
                order_book.book.save()
                messages.success(request, "کتاب با موفقیت به سبد خرید افزوده شد!")
            else:
                messages.error(request, "موجودی کتاب کافی نمی‌باشد!")

    else:
        if check_storage(book, 1) is True:
            order = Order.objects.create(user=request.user)
            order_book = OrderBook.objects.create(book=book, order=order)
            order_book.book.storage -= 1
            order_book.book.sold += 1
            order_book.book.save()
            messages.success(request, "کتاب با موفقیت افزوده شد!")
        else:
            messages.error(request, "کتاب موجود نمی‌باشد.")

    return redirect(request.META['HTTP_REFERER'])


@login_required
def remove_from_cart(request, pk):
    """Checks if there s any active order and orderbook. if there was any, remove an item
    from cart in addition to update storage and sold fields"""
    book = get_object_or_404(Book, pk=pk)
    order_qs = Order.objects.filter(user=request.user, paid=False)
    if order_qs.exists():
        order = order_qs[0]
        if OrderBook.objects.filter(book=book, order=order).exists():
            order_book = OrderBook.objects.get(book=book, order=order)
            if order_book.quantity == 1:
                order_book.delete()
            else:
                order_book.quantity -= 1
                order_book.save()
            order_book.book.storage += 1
            order_book.book.sold -= 1
            order_book.book.save()
            messages.success(request, 'book removed from cart!')
        else:
            messages.error(request, 'there is no such a book!')
    else:
        messages.error(request, 'there is no order')
    return redirect(request.META['HTTP_REFERER'])


# delete_orderbook and update storage and sold fields.
@login_required
def delete_orderbook(request, pk):
    """ If there is order and orderbook, remove it and update storage and sold fields"""
    book = get_object_or_404(Book, pk=pk)
    order_qs = Order.objects.filter(user=request.user, paid=False)
    if order_qs.exists():
        order = order_qs[0]
        if OrderBook.objects.filter(book=book, order=order).exists():
            order_book = OrderBook.objects.get(book=book, order=order)
            order_book.book.storage += order_book.quantity
            order_book.book.sold -= order_book.quantity
            order_book.book.save()
            order_book.delete()
            messages.success(request, 'book removed from cart!')
        else:
            messages.error(request, 'there is no such a book!')
    else:
        messages.error(request, 'there is no order')
    return redirect("home")


# If coupon exists get it. If not return info message.
def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        if coupon.is_active is True:
            return coupon

    except ObjectDoesNotExist:
        messages.info(request, "کد تخفیف وجود ندارد.")
        return redirect(request.META['HTTP_REFERER'])


# If coupon is active, add it to order
class AddCouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(
                    user=self.request.user, paid=False)
                coupon = get_coupon(self.request, code)
                if coupon is None:
                    messages.info(self.request, "کد تخفیف فعال نیست")
                    return redirect(self.request.META['HTTP_REFERER'])
                else:
                    order.coupon = coupon
                    order.save()
                    messages.success(self.request, "Successfully added coupon")
                    return redirect(self.request.META['HTTP_REFERER'])
            except ObjectDoesNotExist:
                messages.info(self.request, "You do not have an active order")
                return redirect(self.request.META['HTTP_REFERER'])
