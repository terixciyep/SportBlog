from django.contrib.auth import get_user_model
from django.db import models
from sport_categories.models import RankForExercise


class UserRank(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ranks = models.ForeignKey(RankForExercise, on_delete=models.CASCADE)
    is_verify = models.BooleanField(default=False)
    verification_file = models.FileField(upload_to='user_ranks_verify_media/')
