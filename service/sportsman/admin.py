from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from sportsman.models import Sport, Sportsman_user

admin.site.register(Sport)
admin.site.register(Sportsman_user)
