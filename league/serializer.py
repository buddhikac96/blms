from rest_framework import serializers
from .models import Match, MatchPlayerConnection


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['type', 'team_one', 'team_two', 'winner', 'team_one_score', 'team_two_score']


class MatchPlayerConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchPlayerConnection
        fields = ['player', 'match', 'score']
