from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    path('cart/update/<int:product_id>/', views.update_cart, name='update_cart'),
    path('cart/checkout/', views.checkout, name="checkout"),
    path('cart/account-information/', views.account_information, name='account-information'),
    path('cart/checkout/payment-information/', views.payment_information, name='payment_information'),
    path('cart(checkout/order_review', views.order_review, name='order_review')
]