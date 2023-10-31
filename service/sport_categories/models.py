from django.db import models


class Sport(models.Model):
    sport_name = models.CharField(max_length=150)

    def __str__(self):
        return self.sport_name


class Exercise(models.Model):
    name = models.CharField(max_length=150)
    measurement_system = models.CharField(max_length=50)
    sport = models.ForeignKey(to=Sport, on_delete=models.PROTECT, related_name='exercises')

    def __str__(self):
        return f"{self.sport}: {self.name} "


class RankForExercise(models.Model):
    rank = (
        ('3 юношеский', 'Третий юношеский спортивный разряд'),
        ('2 юношеский', 'Второй юношеский спортивный разряд'),
        ('1 юношеский', 'Первый юношеский спортивный разряд'),
        ('3 спортивный', 'Третий спортивный разряд'),
        ('2 спортивный', 'Второй спортивный разряд'),
        ('1 спортивный', 'Первый спортивный разряд'),
        ('КМС', 'Кандидат в мастера спорта'),
        ('МС', 'Мастер спорта'),
        ('МСМК', 'мастер спорта России международного класса'),
    )
    rank_fields = models.CharField(choices=rank)
    exercise_standart = models.ForeignKey(to=Exercise, on_delete=models.PROTECT, related_name='ranks')
    standart_mark = models.FloatField()

    def __str__(self):
        return f"{self.rank_fields} | {self.standart_mark} {self.exercise_standart.measurement_system}"


