from django.shortcuts import render

# Create your views here.
offers = [
    {'name': 'Pizza of the month', 'description': 'Introducing our Pizza of the Month: the "Deluxe Feast"! Indulge in a mouthwatering combination of pepperoni, Italian sausage, bacon, bell peppers, tomatoes', 'price': 1090, 'image': '/static/images/pizza_of_the_month.png','location':'http://127.0.0.1:8000/menu/14/'},
    {'name': 'Double Trouble ', 'description': 'Pizza Lair suprise and pepperoni pizza for the price of 2290 kr!', 'price': 2290, 'image': '/static/images/Double_Trouble.png','location':'http://127.0.0.1:8000/menu/15/'},
    {'name': 'Wombo combo', 'description': 'Get a pizza with the side of breadsticks and a soda for a whopping 1990!', 'price': 1990, 'image': '/static/images/wombo_combo.png','location':'http://127.0.0.1:8000/menu/16/'},
]


# Create your views here.
def index(request):
    return render(request, 'offers/index.html', context={'offers': offers})