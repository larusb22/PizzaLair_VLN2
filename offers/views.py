from django.shortcuts import render

# Create your views here.
offers = [
    {'name': 'Family offer', 'description': 'Buy 2 pizzas and get 1 more for free', 'price': 2290},
    {'name': 'La quatro ', 'description': 'Every month 4 of the pizzas on the menu are on the price of 1.000 kr!', 'price': 1000},
    {'name': 'Pizza Madnesss', 'description': 'Hawaiian pizza, Spicy Southwest and Nutella pizza', 'price': 2790},
]


# Create your views here.
def index(request):
    return render(request, 'offers/index.html', context={'offers': offers})