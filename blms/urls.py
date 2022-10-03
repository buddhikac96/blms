from django.contrib import admin
from django.urls import path, include
from team.urls import team_urlpatterns as team_urls
from team.urls import teams_urlpatterns as teams_urls
from user.urls import player_urlpatterns as player_urls
from user.urls import players_urlpatterns as players_urls
from user.urls import coach_urlpatterns as coach_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('team/', include(team_urls)),
    path('teams/', include(teams_urls)),
    path('player/', include(player_urls)),
    path('players/', include(players_urls)),
    path('coach/', include(coach_urls))
]
