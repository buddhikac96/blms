from django.urls import path
from .views import TeamView, TeamsView


team_urlpatterns = [
    path('<int:pk>', TeamView.as_view()),   # get(get team by pk)
    path('', TeamView.as_view()),           # post(create team)
    path('all/', TeamsView.as_view())       # get(get all teams)
]