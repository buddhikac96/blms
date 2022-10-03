from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team
from .serializer import TeamSerializer


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


class TeamListView(APIView):
    # get all teams
    def get(self, request, *args, **kwargs):
        data = Team.objects.all()
        serializer = TeamSerializer(data, many=True)
        if data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('No teams exists', status=status.HTTP_204_NO_CONTENT)
