from django.db import models
from hazvir.models import PlayerInGame
from django.db.models import Count

# Create your models here.

# class Nominacion(models.Model):
#     player = models.ForeignKey(Player, on_delete=models.CASCADE)
#     nominated = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='nominated')
#     votes = models.IntegerField(default=0)
    
#     date = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.player.nickname} nominó a {self.nominated.nickname} ({self.votes} votos)"

# class GalaDeNominacion(models.Model):
#     game = models.ForeignKey(Game, on_delete=models.CASCADE)
#     finished = models.BooleanField(default=False)
#     number = models.IntegerField()
#     nominaciones = models.ManyToManyField(Nominacion, blank=True)
#     players = models.ManyToManyField(Player, blank=True)
    
#     date = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"Nominacion N°{self.number} - {self.game.title}"

class Votacion(models.Model):
    nominados = models.ManyToManyField(PlayerInGame, blank=True)
    name = models.CharField(max_length=50)
    finaliza = models.DateTimeField()
    
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Votación: {self.name}"
    
    def obtener_resultados(self):
        # Calcula los resultados de la votación
        resultados = (
            self.votodelpublico_set
            .values('player__id')  # Obtén el ID del jugador directamente
            .annotate(total_votos=Count('player'))  
            .order_by('-total_votos')
        )
        return resultados

class VotoDelPublico(models.Model):
    player = models.ForeignKey(PlayerInGame, on_delete=models.CASCADE)
    votacion = models.ForeignKey(Votacion, on_delete=models.CASCADE)
    ip = models.CharField(max_length=50)
    visitor_id = models.CharField(max_length=255, default=None, null=True, blank=True)
    
    fecha_voto = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True, default=None)
    
    def __str__(self):
        fecha = self.date.strftime("%d/%m/%Y %H:%M:%S") if self.date else "sin fecha"
        return f"{self.player.player.nickname} - {self.ip} - {fecha}"

