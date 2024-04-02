from rest_framework.viewsets import ModelViewSet
from .models import Player, Game
from .serializers import PlayerSerializer, GameSerializer
from rest_framework import status


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
            queryset = Game.objects.filter(id_name=id_name)
        else:
            queryset = Game.objects.all()
        serializer = GameSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    
    