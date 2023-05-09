from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MenuProduct, CartProduct


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(MenuProduct, id=product_id)
    cart, created = CartProduct.objects.get_or_create(user=request.user)
    cart_product, created = cart.cartproduct_set.get_or_create(product=product)
    if not created:
        cart_product.quantity += 1
        cart_product.save()
    messages.success(request, f'{product.name} has been added to your cart.')
    return redirect('products')


@login_required
def view_cart(request):
    cart_products = CartProduct.objects.filter(user=request.user)
    total = sum(product.total_cost for product in cart_products)
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))
        action = request.POST.get('action')
        cart_product = CartProduct.objects.get(product__id=product_id, user=request.user)
        if action == 'add':
            cart_product.quantity += 1
        elif action == 'remove':
            cart_product.quantity -= 1
        cart_product.save()
        if cart_product.quantity <= 0:
            cart_product.delete()
        return redirect('view_cart')
    return render(request, 'shoppingcart/index.html', {'cart_products': cart_products, 'total': total})


@login_required
def remove_from_cart(request, product_id):
    cart_product = get_object_or_404(CartProduct, product__id=product_id, user=request.user)
    cart_product.delete()
    messages.success(request, f'{cart_product.product.name} has been removed from your cart.')
    return redirect('view_cart')


@login_required
def clear_cart(request):
    cart_products = CartProduct.objects.filter(user=request.user)
    cart_products.delete()
    messages.success(request, 'Your cart has been cleared.')
    return redirect('view_cart')
