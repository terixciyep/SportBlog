from django.contrib.auth.models import User
from django.db import models

class Sport(models.Model):
    sport = models.CharField(max_length=100)

    def __str__(self):
        return self.sport

class Sportsman_user(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    favorite_sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} {self.last_name}"
