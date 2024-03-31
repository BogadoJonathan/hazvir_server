from django.db import models
from hazvir.models import Player, Game
# Create your models here.

class Nominacion(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    nominated = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='nominated')
    votes = models.IntegerField(default=0)
    
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.player.nickname} nominó a {self.nominated.nickname} ({self.votes} votos)"

class GalaDeNominacion(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    finished = models.BooleanField(default=False)
    number = models.IntegerField()
    nominaciones = models.ManyToManyField(Nominacion, blank=True)
    players = models.ManyToManyField(Player, blank=True)
    
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Nominacion N°{self.number} - {self.game.title}"

class GalaEliminacion(models.Model):
    nominados = models.ManyToManyField(Player, blank=True)
    gala = models.ForeignKey(GalaDeNominacion, on_delete=models.CASCADE)
    finaliza = models.DateTimeField()
    
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Nominados de la gala {self.gala.number}"

class votoDelPublico(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    GalaEliminacion = models.ForeignKey(GalaEliminacion, on_delete=models.CASCADE)
    ip = models.CharField(max_length=50)
    
    fecha_voto = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"Voto para {self.player.nickname}"

