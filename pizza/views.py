from django.shortcuts import render
pizzas = [
    {'name': 'margherita', 'price': 9.99},
    {'name': 'pepperoni', 'price': 12.99},
]
# Create your views here.
def index(request):
    """The home page for Pizza Lair."""
    return render(request, 'pizza/index.html', context=
    { 'pizzas': pizzas })