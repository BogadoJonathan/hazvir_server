from rest_framework.viewsets import ModelViewSet
from .models import Player, Game
from .serializers import PlayerSerializer, GameSerializer

class PlayerView(ModelViewSet):
    http_method_names = ['get']
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

class GameView(ModelViewSet):
    http_method_names = ['get']
    serializer_class = GameSerializer
    queryset = Game.objects.all()