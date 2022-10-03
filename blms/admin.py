from django.contrib import admin
from team.models import Team
from user.models import Player, Coach


admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Coach)
