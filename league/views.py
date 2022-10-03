from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Match, MatchPlayerConnection
from .serializer import MatchSerializer, MatchPlayerConnectionSerializer


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