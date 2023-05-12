from django.db import models
from menu.models import MenuProduct
from offers.models import Offers


# Create your models here.

class OrderedProduct(models.Model):
    product = models.ForeignKey(MenuProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE)