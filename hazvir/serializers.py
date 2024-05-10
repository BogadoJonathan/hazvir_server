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
    player_name = serializers.SerializerMethodField()
    
    class Meta:
        model = PlayerInGame
        fields = '__all__'
    
    def get_player_name(self, obj):
        return obj.player.nickname if obj.player else None

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
