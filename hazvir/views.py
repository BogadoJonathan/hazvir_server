from rest_framework.viewsets import ModelViewSet
from .models import Player, Game, PlayerInGame
from .serializers import PlayerSerializer, GameSerializer, PlayerInGameSerializer
from rest_framework import status
from rest_framework.response import Response


class PlayerView(ModelViewSet):
    http_method_names = ['get']
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

class GameView(ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    
    def list(self, request):
        id_name = request.query_params.get('id_name', None)
        if id_name is not None:
            queryset = self.queryset.filter(id_name=id_name)
        else:
            queryset = self.queryset
        serializer = GameSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class PlayerInGameView(ModelViewSet):
    serializer_class = PlayerInGameSerializer
    queryset = PlayerInGame.objects.all()
    
    def list(self, request):
        game_id = request.query_params.get('game_id', None)
        if game_id is not None:
            queryset = self.queryset.filter(game=game_id)
        else:
            queryset = self.queryset
        serializer = PlayerInGameSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    