# able to create games/matches through the admin 
from django.contrib import admin

from .models import Matches, Game, Leaderboard # matches and games models
# Register your models here.

admin.site.register(Matches) # able to add matches in the admin user interface 
admin.site.register(Game) # able to add games in the admin user interface
admin.site.register(Leaderboard)