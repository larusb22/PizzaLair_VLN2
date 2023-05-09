from django.shortcuts import render, get_object_or_404
from menu.models import MenuProduct


# Create your views here.
def index(request):
    context = {'products': MenuProduct.objects.all().order_by('name')}
    return render(request, 'menu/index.html', context)


def get_product_by_id(request, id):
    return render(request, 'menu/product_detail.html', {
        'product': get_object_or_404(MenuProduct, pk=id)
    })

