from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MenuProduct


def add_to_cart(request, product_id):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    cart = request.session['cart']
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    request.session.modified = True
    return redirect('view_cart')


def view_cart(request):
    if 'cart' not in request.session:
        cart = {}
    else:
        cart = request.session['cart']
    products_in_cart = []
    total = 0
    for prodid, quantity in cart.items():
        prod = MenuProduct.objects.filter(id=prodid).first()
        if prod:
            product_total = prod.price * quantity
            total += product_total
            products_in_cart.append({
                'product': prod,
                'quantity': quantity,
                'total': product_total,
            })
    return render(request, 'shoppingcart/index.html', context={
        'cartitems': products_in_cart,
        'total': total,
    })


def update_cart(request, product_id):
    print(product_id)
    if 'cart' not in request.session:
        return redirect('view_cart')
    try:
        cart = request.session['cart']
        quantity = int(request.POST['quantity'])
        if quantity > 0:
            cart[product_id] = quantity
        else:
            del cart[product_id]
        request.session.modified = True
    except (KeyError, ValueError):
        pass
    return redirect('view_cart')


def remove_from_cart(request, product_id):
    if 'cart' not in request.session:
        return redirect('view_cart')
    try:
        cart = request.session['cart']
        if str(product_id) in cart:
            del cart[str(product_id)]
            messages.success(request, 'Product removed from cart')
        request.session.modified = True
    except ValueError:
        pass
    return redirect('view_cart')



def clear_cart(request):
    if 'cart' in request.session:
        request.session['cart'] = {}
    return redirect('view_cart')
