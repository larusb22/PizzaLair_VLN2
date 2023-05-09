from django.db import models
from menu.models import MenuProduct
from account.models import AccountUser


# Create your models here.

class ShoppingCart(models.Model):
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)


class CartProduct(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(MenuProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
