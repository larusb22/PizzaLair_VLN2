from django.shortcuts import render

# Create your views here.
offers = [
    {'name': 'Family Offer', 'description': 'Buy 2 pizzas and get 1 more for free', 'price': 2290, 'image': '/static/images/maximillian.png'},
    {'name': 'La Quatro ', 'description': 'Every month 4 of the pizzas on the menu are on the price of 1.000 kr!', 'price': 1000, 'image': '/static/images/la_quatro_final.png'},
    {'name': 'Pizza Madness', 'description': 'Hawaiian pizza, Spicy Southwest and Nutella pizza', 'price': 2790, 'image': '/static/images/pizza_madness.png'},
]


# Create your views here.
def index(request):
    return render(request, 'offers/index.html', context={'offers': offers})