from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User, AbstractUser
from django.db import models

class Sport(models.Model):
    sport = models.CharField(max_length=100)

    def __str__(self):
        return self.sport

class UserManager(BaseUserManager):

    def create_user(self, email, password=None):

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class Sportsman_user(AbstractUser):
    username = models.CharField(
        "username",
        max_length=150,
        unique=False,
        help_text=
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages={"unique": "A user with that username already exists."},
    )
    email_verify = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    favorite_sport = models.ForeignKey(Sport, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return f"{self.email}"
