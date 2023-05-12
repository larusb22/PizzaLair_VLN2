from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='menu-index'),
    path('types/<int:type_id>/', views.types, name='menu-types'),
    path('<int:product_id>/', views.get_product_by_id, name='product-details'),
]

