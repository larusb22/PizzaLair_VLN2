from django.shortcuts import render

# Create your views here.
offers = [
    {'name': '2 For 1 ', 'description': '', 'price': 9.99},
    {'name': 'Meat Fiesta', 'description': '', 'price': 10.99},
]
# Create your views here.
def index(request):
    return render(request, 'offers/index.html', context={'offers': offers})