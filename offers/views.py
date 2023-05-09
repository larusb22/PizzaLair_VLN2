from django.shortcuts import render

# Create your views here.
offers = [
    {'name': '2 For 1 ', 'description': 'Buy 1 and get 2', 'price': 14.99},
    {'name': 'Meat Fiesta', 'description': 'A lot of meat', 'price': 15.99},
]
# Create your views here.
def index(request):
    return render(request, 'offers/index.html', context={'offers': offers})