from django.contrib.auth.models import User, AbstractUser
from django.db import models

class Sport(models.Model):
    sport = models.CharField(max_length=100)

    def __str__(self):
        return self.sport

class Sportsman_user(AbstractUser):
    username = models.CharField(
        "username",
        max_length=150,
        unique=False,
        help_text=
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages={"unique": "A user with that username already exists."},
    )
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    favorite_sport = models.ForeignKey(Sport, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return f"{self.name} {self.last_name}"
