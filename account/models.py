from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class AccountUser(models.Model):
    email = models.CharField(max_length=255, unique="")  # Þarf að bæta ehv við
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Countries(models.Model):
    name = models.CharField(max_length=255)


class UserAddress(models.Model):
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    house_address = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)


class RegisterUser(models.Model):
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_image = models.CharField(max_length=9999)
