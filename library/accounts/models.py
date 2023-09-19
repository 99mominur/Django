from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator
from .managers import UserManager
from .constants import GENDER_CHOICE

# Create your models here.


class User(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True, null=False, blank=True)
    objects = UserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


class LibraryAccountType(models.Model):
    name = models.CharField(max_length=30)
    max_borrow_books = models.IntegerField(max=3)

    def __str__(self):
        return self.name


class UserLibraryAccounts(models.Model):
    user = models.OneToOneField(
        User, related_name="account", on_delete=models.CASCADE)
    account_type = models.ForeignKey(
        LibraryAccountType, related_name="accounts", on_delete=models.CASCADE)
    account_no = models.PositiveIntegerField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    birth_date = models.DateField(null=False, blank=True)

    def __str__(self):
        return str(self.account_no)


class UserAddress(models.Model):
    user = models.OneToOneField(
        User, related_name="address", on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.user.email