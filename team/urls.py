from django.urls import path
from .views import TeamView, TeamListView, TeamStats90thPercentile


team_urlpatterns = [
    path('<int:pk>', TeamView.as_view()),   # get(get team by pk)
    path('', TeamView.as_view()),           # post(create team)
    path('all/', TeamListView.as_view()),       # get(get all teams)
    path('stats/90thpercentile/<int:pk>', TeamStats90thPercentile.as_view())
]