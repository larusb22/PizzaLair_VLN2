from django.db import models


# Create your models here.
class MenuRating(models.Model):
    rating = models.FloatField()
    total_ratings = models.IntegerField()


class MenuType(models.Model):  # Product Type (spicy eða eh þannig)
    name = models.CharField(max_length=255)


class MenuToppingType(models.Model):
    name = models.CharField(max_length=255)


class MenuTopping(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(MenuToppingType, on_delete=models.CASCADE)  # Kannski hafa foreign key í Type klasann


class MenuSize(models.Model):
    name = models.CharField(max_length=255)  # fyrir small, medium og large


class MenuProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    rating = models.ForeignKey(MenuRating, on_delete=models.CASCADE)
    type = models.ForeignKey(MenuType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MenuProductTopping(models.Model):
    menu = models.ForeignKey(MenuProduct, on_delete=models.CASCADE)
    topping = models.ForeignKey(MenuTopping, on_delete=models.CASCADE)


class MenuProductPrice(models.Model):  # spurja kennara út í
    price = models.FloatField()
    menu = models.ForeignKey(MenuProduct, on_delete=models.CASCADE)
    size = models.ForeignKey(MenuSize, on_delete=models.CASCADE)


class MenuImage(models.Model):
    image = models.CharField(max_length=9999)
    menu = models.ForeignKey(MenuProduct, on_delete=models.CASCADE)

    def __str__(self):
        return self.image
