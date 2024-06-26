from django.utils import timezone
from datetime import timedelta
from rest_framework.viewsets import ModelViewSet
from .models import Votacion, VotoDelPublico
from .serializers import VotoDelPublicoSerializer, VotacionSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

class VotacionView(ModelViewSet):
    http_method_names = ['get']
    serializer_class = VotacionSerializer
    queryset = Votacion.objects.all()

class VotoDelPublicoView(ModelViewSet):
    http_method_names = ['post']
    serializer_class = VotoDelPublicoSerializer
    queryset = VotoDelPublico.objects.all()
    
    def create(self, request):
        ip_address = request.META.get('HTTP_X_REAL_IP')
        visitor_id = request.data.get('visitor_id', None)
        
        if not ip_address:
            return Response({'error': 'No se ha enviado la dirección IP.'}, status=status.HTTP_400_BAD_REQUEST)
        if not visitor_id:
            return Response({'error': 'No se ha enviado el visitor_id.'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        ip_votes = VotoDelPublico.objects.filter(ip=ip_address, fecha_voto__gte=timezone.now() - timedelta(hours=12))
        if ip_votes.exists():
            return Response({'error': 'Tú o tu hogar ya han votado en las últimas 12 horas.'}, status=status.HTTP_400_BAD_REQUEST)
        visitor_votes = VotoDelPublico.objects.filter(visitor_id=visitor_id, fecha_voto__gte=timezone.now() - timedelta(hours=12))
        if visitor_votes.exists():
            return Response({'error': 'Ya has votado en las últimas 12 horas.'}, status=status.HTTP_400_BAD_REQUEST)
        #el VotoDelPublico tiene asociado el modelo: Votacion, donde ahi se muestra a las personas a quien se pueda votar
        #por lo que se debe hacer una validacion para que el voto sea valido, recibiremos el id de la votacion, la buscamos y verificamos el voto
        
        votacion_id = request.data.get('votacion', None)
        if not votacion_id:
            return Response({'error': 'No se ha enviado la votación.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            votacion = Votacion.objects.get(pk=votacion_id)
        except:
            return Response({'error': 'La votación no existe.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if votacion.finaliza < timezone.now():
            return Response({'error': 'La votación ha finalizado.'}, status=status.HTTP_400_BAD_REQUEST)
        id_player = request.data.get('player', None)
        if not votacion.nominados.filter(pk=id_player).exists():
            return Response({'error': 'El jugador no está en la votación.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(ip=ip_address)
        serializer.save(visitor_id=visitor_id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)