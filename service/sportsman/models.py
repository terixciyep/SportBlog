from django.contrib.auth.models import User, AbstractUser
from django.db import models

class Sport(models.Model):
    sport = models.CharField(max_length=100)

    def __str__(self):
        return self.sport

class Sportsman_user(AbstractUser):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    favorite_sport = models.ForeignKey(Sport, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f"{self.name} {self.last_name}"
