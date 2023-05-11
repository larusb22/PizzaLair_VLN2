from django.shortcuts import render, get_object_or_404
from menu.models import MenuProduct, MenuProductTopping, MenuTopping, MenuType


def index(request):
    context = {
        'products': MenuProduct.objects.all().order_by('name'),
        'types': MenuType.objects.all()
    }
    return render(request, 'menu/index.html', context)


def get_product_by_id(request, id):
    return render(request, 'menu/product_detail.html', {
        'product': get_object_or_404(MenuProduct, pk=id)
    })


def get_toppings(request, menu_id):
    return render(request, 'menu/product_detail.html', {
        'topping': get_object_or_404(MenuProductTopping, pk=menu_id)
    })


def types(request, type_id=None):
    selected_type = None
    products = MenuProduct.objects.all().order_by('name')

    if type_id is not None:
        selected_type = get_object_or_404(MenuType, pk=type_id)
        products = products.filter(type=selected_type)

    context = {
        'products': products,
        'types': MenuType.objects.all(),
        'selected_type': selected_type
    }
    return render(request, 'menu/index.html', context)
