from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from sportsman.models import Sportsman_user
from services.serializers import AthleteSerializer


class AthleteInfoView(ReadOnlyModelViewSet):
    queryset = Sportsman_user.objects.all()
    serializer_class = AthleteSerializer


def send_email(request):
    return HttpResponse('ok')