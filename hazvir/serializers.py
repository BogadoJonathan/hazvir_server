from rest_framework import serializers
from .models import Player, Game, PlayerInGame, Score, Post

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class PlayerInGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerInGame
        fields = '__all__' + ['player_name']
