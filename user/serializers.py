from rest_framework import serializers
from .models import Player, Coach


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["name", "height", "team", "game_count"]


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ["name", "team"]