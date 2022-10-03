from django.core.validators import MinValueValidator
from django.db import models
from team.models import Team
from user.models import Player
from django.utils.translation import gettext_lazy as _


class Match(models.Model):
    class MatchType(models.TextChoices):
        QUALIFIER = 'QR', _('Qualifier Round')
        QUARTERFINAL = 'QF', _('Quarter Final')
        SEMIFINAL = 'SF', _('Semi Final')
        FINAL = 'F', _('Final')

    type = models.CharField(max_length=2, choices=MatchType.choices)
    team_one = models.ForeignKey(Team, related_name='team_one', on_delete=models.CASCADE)
    team_two = models.ForeignKey(Team, related_name='team_two', on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, related_name='winner', on_delete=models.CASCADE)
    team_one_score = models.IntegerField(validators=[MinValueValidator(0)])
    team_two_score = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.team_one.name + ' vs ' + self.team_two.name


class MatchPlayerConnection(models.Model):
    player = models.ForeignKey(Player, related_name='player', on_delete=models.CASCADE)
    match = models.ForeignKey(Match, related_name='match', on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.score
