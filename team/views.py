import math

from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team
from .serializer import TeamSerializer
from user.models import Player
from league.models import MatchPlayerConnection
from user.serializers import PlayerSerializer


class TeamView(APIView):
    # Get team by pk
    def get(self, request, pk, *args, **kwargs):
        data = get_object_or_404(Team, pk=pk)
        serializer = TeamSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create team
    def post(self, request, *ags, **kwargs):
        data = {
            'name': request.data.get('name'),
            'short_name': request.data.get('short_name'),
            'owner': request.data.get('owner')
        }

        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Team, pk=pk)
        data = {
            'name': request.data.get('name'),
            'short_name': request.data.get('short_name'),
            'owner': request.data.get('owner')
        }
        serializer = TeamSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Team ' + instance.name + ' updated',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Team, pk=pk)
        instance.delete()
        return Response({
            'message': 'Team ' + instance.name + ' deleted'
        }, status=status.HTTP_200_OK)


class TeamListView(APIView):
    # get all teams
    def get(self, request, *args, **kwargs):
        data = Team.objects.all()
        serializer = TeamSerializer(data, many=True)
        if data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('No teams exists', status=status.HTTP_204_NO_CONTENT)


class TeamStats90thPercentile(APIView):
    def get(self, request, pk, *args, **kwargs):
        players = []
        player_pks = []
        team_players = Player.objects.filter(team=pk)
        # get player averages
        for player in team_players:
            total = 0
            pm_cons = MatchPlayerConnection.objects.filter(player=player.pk)
            # calculate player total
            for pm_con in pm_cons:
                total += pm_con.score
            average = total / player.game_count if player.game_count > 0 else 0
            players.append({
                'pk': player.pk,
                'average': average
            })

        sorted_players = sorted(players, key=lambda l: l['average'])
        percentile_90th = math.floor(len(players) * 0.9)

        for i in range(percentile_90th - 1, len(players)):
            player_pks.append(sorted_players[i]['pk'])

        data = Player.objects.filter(pk__in=player_pks)
        serializer = PlayerSerializer(data, many=True)
        return Response({
            'message': '90th Percentile Players',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
