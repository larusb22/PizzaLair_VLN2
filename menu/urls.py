from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='menu-index'),
    path('<int:product_id>', views.get_product_by_id, name='product-details')
]