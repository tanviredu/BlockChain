from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
    User,
)


class UserProfilemanager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User Must Have Email")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    ## login with email
    ## so we add a field email
    ## go to the AbstractBaseUser
    ## and PermissionMixin base class to see the code
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    ## this class have to access the usernamaner
    ## with something like this
    ## UserProfile.objects.action()
    ## malke this

    objects = UserProfilemanager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


class Ingredient(models.Model):
    salad = models.IntegerField(default=0)
    cheese = models.IntegerField(default=0)
    meat = models.IntegerField(default=0)

    def __str__(self):
        return str(self.salad) + str(self.cheese) + str(self.meat)


class CustomerDetail(models.Model):
    deliveryAddress = models.TextField(blank=True)
    phone = models.CharField(max_length=255, blank=True)
    paymentType = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.deliveryAddress


class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    ingredients = models.OneToOneField(Ingredient, on_delete=models.CASCADE, null=True)
    customer_detail = models.OneToOneField(
        CustomerDetail, on_delete=models.CASCADE, null=True
    )
    price = models.CharField(max_length=20, blank=True)
    orderTime = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return str(self.user) + "Order"
