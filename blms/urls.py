from django.contrib import admin
from django.urls import path, include
from team.urls import team_urlpatterns as team_urls
from user.urls import player_urlpatterns as player_urls
from user.urls import coach_urlpatterns as coach_urls
from league.urls import match_urlpatterns as match_urls
from league.urls import match_player_connection_urlpatterns as m_p_urls
from user.urls import player_stats_urlpatterns as player_stats_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('team/', include(team_urls)),
    path('player/', include(player_urls)),
    path('player/stats/', include(player_stats_urls)),
    path('coach/', include(coach_urls)),
    path('match/', include(match_urls)),
    path('mpcon/', include(m_p_urls))
]
