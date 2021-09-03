from django.urls import path
from .views import *

urlpatterns = [
    path('add_to_cart/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('delete_orderbook/<int:pk>/', delete_orderbook, name='delete_orderbook'),
    path('order_summary/', OrderSummaryView.as_view(), name="order_summary"),
    path('checkout/', CheckoutFormView.as_view(), name="checkout"),
    path('add_coupon/', AddCouponView.as_view(), name="add_coupon"),
    path('get_coupon/', get_coupon, name="get_coupon"),
]