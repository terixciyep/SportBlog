from rest_framework import serializers

from sportsman.models import Sportsman_user

from rest_framework import serializers

from sportsman.models import Sportsman_user

class AthleteSerializer(serializers.ModelSerializer):
    athlete_name = serializers.CharField(source='name')
    athlete_last_name = serializers.CharField(source='last_name')
    favorite_sport_athlete = serializers.CharField(source='favorite_sport')

    class Meta:
        model = Sportsman_user
        fields = ('id', 'favorite_sport_athlete', 'athlete_name', 'athlete_last_name')




