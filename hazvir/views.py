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
    http_method_names = ['get']
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    
    def list(self, request):
        id_name = request.query_params.get('id_name', None)
        if id_name is not None:
            queryset = self.queryset.filter(id_name=id_name)
            if not queryset.exists():
                return Response({'error': 'The game does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            queryset = self.queryset
        serializer = GameSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class PlayerInGameView(ModelViewSet):
    http_method_names = ['get']
    serializer_class = PlayerInGameSerializer
    queryset = PlayerInGame.objects.all()
    
    def list(self, request):
        game_id = request.query_params.get('game_id', None)
        players = request.query_params.get('id_players', None)
        
        if game_id is not None:
            queryset = self.queryset.filter(game=game_id)
        elif players is not None:
            if type(players) is not list:
                return Response({'error': 'id_players must be a list.'}, status=status.HTTP_400_BAD_REQUEST)
            players = players.split(',')
            queryset = self.queryset.filter(pk__in=players)
        else:
            queryset = self.queryset
        serializer = PlayerInGameSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)