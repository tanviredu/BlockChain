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

    USERNAME_FIELD = "email"

    ## this class have to access the usernamaner
    ## with something like this
    ## UserProfile.objects.action()
    ## malke this
    objects = UserProfilemanager()

    def __str__(self):
        return self.email
