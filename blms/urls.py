from django.contrib import admin
from django.urls import path, include
from team.urls import team_urlpatterns as team_urls
from team.urls import teams_urlpatterns as teams_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('team/', include(team_urls)),
    path('teams/', include(teams_urls))
]
