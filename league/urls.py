from django.urls import path
from .views import MatchView, MatchesView, MatchPlayerConnectionView, MatchPlayerConnectionListView


match_urlpatterns = [
    path('', MatchView.as_view()),               # get(get match by pk)
    path('<int:pk>', MatchView.as_view()),       # post(create a match)
    path('all/', MatchesView.as_view())          # get(get all matches)
]

match_player_connection_urlpatterns = [
    path('<int:pk>', MatchPlayerConnectionView.as_view()),   # get(get match player connection by pk)
    path('', MatchPlayerConnectionView.as_view()),           # post(create match player connection)
    path('all/', MatchPlayerConnectionListView.as_view())
]
