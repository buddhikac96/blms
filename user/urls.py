from django.urls import path
from .views import PlayerView, PlayerListView, CoachView, CoachTeamView

player_urlpatterns = [
    path('<int:pk>', PlayerView.as_view()),
    path('', PlayerView.as_view())
]

players_urlpatterns = [
    path('team/<int:pk>', PlayerListView.as_view())
]

coach_urlpatterns = [
    path('<int:pk>', CoachView.as_view()),              # get(get coach by coach_pk)
    path('', CoachView.as_view()),                      # post(create a coach)
    path('team/<int:pk>', CoachTeamView.as_view())      # get(get coach by team_pk)
]
