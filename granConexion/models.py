from django.db import models
from hazvir.models import PlayerInGame
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
    name = models.models.CharField(max_length=50)
    finaliza = models.DateTimeField()
    
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Votación: {self.gala}"

class VotoDelPublico(models.Model):
    player = models.ForeignKey(PlayerInGame, on_delete=models.CASCADE)
    votacion = models.ForeignKey(Votacion, on_delete=models.CASCADE)
    ip = models.CharField(max_length=50)
    
    fecha_voto = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"Voto para {self.player.player.nickname}"

