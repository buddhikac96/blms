from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Match, MatchPlayerConnection
from .serializer import MatchSerializer, MatchPlayerConnectionSerializer
from user.models import Player


class MatchView(APIView):
    def get(self, request, pk, *args, **kwargs):
        data = get_object_or_404(Match, pk=pk)
        serializer = MatchSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'type': request.data.get('type'),
            'team_one': request.data.get('team_one'),
            'team_two': request.data.get('team_two'),
            'winner': request.data.get('winner'),
            'team_one_score': request.data.get('team_one_score'),
            'team_two_score': request.data.get('team_two_score')
        }

        serializer = MatchSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MatchesView(APIView):
    # Get all matches
    def get(self, request, *args, **kwargs):
        data = Match.objects.all()
        if data:
            serializer = MatchSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("No matches", status=status.HTTP_204_NO_CONTENT)


class MatchPlayerConnectionView(APIView):
    # Get match player connection by pk
    def get(self, request, pk, *args, **kwargs):
        data = get_object_or_404(MatchPlayerConnection, pk=pk)
        serializer = MatchPlayerConnectionSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'player': request.data.get('player'),
            'match': request.data.get('match'),
            'score': request.data.get('score')
        }

        serializer = MatchPlayerConnectionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            self.update_player_game_count(data['player'])
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update_player_game_count(player_pk):
        player_data = Player.objects.get(pk=player_pk)
        player_data.game_count += 1
        player_data.save()


class MatchPlayerConnectionListView(APIView):
    # Get all match player connections
    def get(self, request, *args, **kwargs):
        data = MatchPlayerConnection.objects.all()
        if data:
            serializer = MatchPlayerConnectionSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("No match player connections", status=status.HTTP_204_NO_CONTENT)