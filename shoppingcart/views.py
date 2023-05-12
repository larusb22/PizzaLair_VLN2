from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MenuProduct
from account.forms import UnregisteredUserForm, RegisteredUserForm, CreditCardForm
from django.contrib.auth.models import User


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


def checkout(request):
    print("Checkout function is being called")
    if 'cart' not in request.session:
        return redirect('view_cart')
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
    return render(request, 'shoppingcart/account_information.html', context={
        'cartitems': products_in_cart,
        'total': total,
    })


def account_information(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = RegisteredUserForm(request.POST)
            account_info = form.save(commit=False)
            account_info.user = request.user
        else:
            form = UnregisteredUserForm(request.POST)
            if form.is_valid():
                account_info = form.save(commit=False)
                if request.user.is_authenticated:
                    account_info.user = request.user
                account_info.first_name = form.cleaned_data['first_name']
                account_info.last_name = form.cleaned_data['last_name']
                account_info.save()
        if form.is_valid():
            account_info.save()
    else:
        if request.user.is_authenticated:
            form = RegisteredUserForm()
        else:
            form = UnregisteredUserForm()
    return render(request, 'shoppingcart/account_information.html', {'form': form})


def payment_information(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            return render(request, 'shoppingcart/order_review.html')
    else:
        form = CreditCardForm()
    return render(request, 'shoppingcart/payment_information.html', {'form': form})


def order_review(request):
    return render(request, 'shoppingcart/order_review.html')
