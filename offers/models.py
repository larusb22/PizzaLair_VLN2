from django.db import models
from menu.models import MenuProduct


# from menu.models import MenuRating

# Create your models here.

# Spurning hvort það ætti að vera sér rating fyrir Offers og fyrir Product?

class OfferRating(models.Model):
    rating = models.FloatField()
    total_ratings = models.IntegerField()


class Offers(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=400)  # Getur verið lengra
    rating = models.ForeignKey(OfferRating, on_delete=models.CASCADE)
    product = models.ForeignKey(MenuProduct, on_delete=models.CASCADE)


