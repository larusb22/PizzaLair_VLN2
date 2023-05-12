from django.db import models
from menu.models import MenuProduct


# from menu.models import MenuRating

# Create your models here.

# Spurning hvort það ætti að vera sér rating fyrir Offers og fyrir Product?

class ProductsInOffer(models.Model):
    pass



class Offers(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=400)  # Getur verið lengra
    price = models.DecimalField(decimal_places=0, max_digits=8, default=1490)
    products = models.ForeignKey(ProductsInOffer, on_delete=models.CASCADE)
    offer_image = models.CharField(max_length=9999, default='')

