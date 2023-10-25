from django.contrib import admin

from sportsman.models import Sport, Sportsman_user

admin.site.register(Sportsman_user)
admin.site.register(Sport)
