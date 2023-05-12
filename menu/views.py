from django.shortcuts import render, get_object_or_404
from menu.models import MenuProduct, MenuProductTopping, MenuTopping, MenuType


def index(request):
    context = {
        'products': MenuProduct.objects.all().order_by('name'),
        'types': MenuType.objects.all(),
    }
    return render(request, 'menu/index.html', context)


def get_product_by_id(request, product_id):
    product = get_object_or_404(MenuProduct, pk=product_id)
    toppings = get_toppings(product_id)
    context = {'product': product, 'toppings': toppings}
    return render(request, 'menu/product_detail.html', context)


def get_toppings(product_id):
    toppings = MenuProductTopping.objects.filter(menu=product_id).select_related('topping')
    topping_names = [t.topping.name for t in toppings]
    return topping_names


def types(request, type_id=None):
    selected_type = None
    products = MenuProduct.objects.all().order_by('name')

    if type_id is not None:
        selected_type = get_object_or_404(MenuType, pk=type_id)
        products = products.filter(type=selected_type)

    context = {
        'products': products,
        'types': MenuType.objects.all(),
        'selected_type': selected_type,
    }
    return render(request, 'menu/index.html', context)

