from django import forms
from .models import OrderedProduct


class OrderedProductForm(forms.ModelForm):
    class Meta:
        model = OrderedProduct
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.HiddenInput(),
        }
