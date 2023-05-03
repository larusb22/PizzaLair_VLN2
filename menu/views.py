from django.shortcuts import render

pizzas = [
    {'name': 'Margherita', 'price': 9.99},
    {'name': 'Pepperoni', 'price': 11.99},
    {'name': 'Hawaiian', 'price': 12.99},
    {'name': 'Meat Lovers', 'price': 13.99},
    {'name': 'Vegetarian', 'price': 10.99},
]
# Create your views here.
def index(request):
    return render(request, 'menu/index.html', context={'pizzas': pizzas})