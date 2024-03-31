from django.contrib import admin
from .models import Player, Game, PlayerInGame, Score, Post

# Register your models here.
admin.site.register(Player)
admin.site.register(Game)
admin.site.register(PlayerInGame)
admin.site.register(Score)
admin.site.register(Post)