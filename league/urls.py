from django.urls import path
from .views import MatchView, MatchesView


match_urlpatterns = [
    path('', MatchView.as_view()),               # get(get match by pk)
    path('<int:pk>', MatchView.as_view()),       # post(create a match)
    path('all/', MatchesView.as_view())          # get(get all matches)
]

match_player_connection_urlpatterns = [

]
