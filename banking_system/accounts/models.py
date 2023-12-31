from decimal import Decimal
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .managers import UserManager
from .constants import GENDER_CHOICE

# Create your models here.


class User(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True, null=False, blank=True)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    @property
    def balance(self):
        if hasattr(self, "account"):
            return self.account.balance
        return 0


class BankAccountType(models.Model):
    name = models.CharField(max_length=30)
    maximum_withdrawal_amount = models.DecimalField(
        max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class UserBankAccount(models.Model):
    user = models.OneToOneField(
        User, related_name="account", on_delete=models.CASCADE)
    accout_type = models.ForeignKey(
        BankAccountType, related_name="accounts", on_delete=models.CASCADE)
    account_no = models.PositiveIntegerField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    birth_date = models.DateField(null=True, blank=True)
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    initial_deposite_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.account_no)


class UserAddress(models.Model):
    user = models.OneToOneField(
        User, related_name="address", on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.PositiveIntegerField()
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.email
