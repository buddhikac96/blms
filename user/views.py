from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Player, Coach
from .serializers import PlayerSerializer, CoachSerializer
from league.models import MatchPlayerConnection


class PlayerView(APIView):
    # Get player by pk
    def get(self, request, pk, *args, **kwargs):
        data = get_object_or_404(Player, pk=pk)
        serializer = PlayerSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create a player
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'height': request.data.get('height'),
            'team': request.data.get('team')
        }

        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        player = get_object_or_404(Player, pk=pk)
        data = {
            'name': request.data.get('name'),
            'height': request.data.get('height'),
            'team': request.data.get('team')
        }
        serializer = PlayerSerializer(instance=player, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Player, pk=pk)
        instance.delete()
        return Response('Player deleted', status=status.HTTP_200_OK)


class PlayerListView(APIView):
    # Get all players by team
    def get(self, request, pk, *args, **kwargs):
        data = Player.objects.filter(team=pk)
        if data:
            serializer = PlayerSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('No players', status=status.HTTP_204_NO_CONTENT)


class PlayerStatsAvg(APIView):
    # Get player average by player_pk
    def get(self, request, pk, *args, **kwargs):
        player = get_object_or_404(Player, pk=pk)
        mp_con_list = MatchPlayerConnection.objects.filter(player=pk)

        total = 0
        for mp_con in mp_con_list:
            total += mp_con.score

        average = total / player.game_count if player.game_count > 0 else 0
        return Response({
            'message': 'Player Average',
            'data': average
        }, status=status.HTTP_200_OK)


class CoachView(APIView):
    # Get coach by pk
    def get(self, request, pk, *args, **kwargs):
        data = get_object_or_404(Coach, pk=pk)
        serializer = CoachSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create a coach
    def post(self, request, *args, **kwargs):
        # Validate team already has a coach
        team_coach = Coach.objects.filter(team=request.data.get('team'))
        if team_coach:
            return Response('Coach already exist', status=status.HTTP_208_ALREADY_REPORTED)

        data = {
            'name': request.data.get('name'),
            'team': request.data.get('team')
        }

        serializer = CoachSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CoachTeamView(APIView):
    # Get coach by team pk
    def get(self, request, pk, *args, **kwargs):
        data = get_object_or_404(Coach, team=pk)
        serializer = CoachSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
