from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from team.models import Team


class Player(models.Model):
    name = models.CharField(max_length=200)
    # height in centimeters
    height = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(300)], default=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    game_count = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return self.name


class Coach(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name