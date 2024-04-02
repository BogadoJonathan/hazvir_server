from rest_framework.viewsets import ModelViewSet
from .models import Player, Game
from .serializers import PlayerSerializer, GameSerializer
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
        serializer = GameSerializer(self.queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    
    