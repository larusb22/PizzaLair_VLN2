from django.db import models
from menu.models import MenuProduct
from account.models import AccountUser


# Create your models here.

class Countries(models.Model):
    country = models.CharField(max_length=255)


class Order(models.Model):
    order_status = models.CharField(max_length=255)
    date = models.DateTimeField()
    paid = models.BooleanField()
    total_price = models.DecimalField(max_digits=8)
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)


class OrderedProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(MenuProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField()
