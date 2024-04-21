from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from PIL import Image
import os

class ImageModel(models.Model):
    
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = self.__class__.objects.get(pk=self.pk)
            except self.__class__.DoesNotExist:
                pass
            else:
                # Si la instancia anterior tiene una imagen y la nueva imagen es diferente, elimina la anterior
                if old_instance.image and old_instance.image != self.image:
                    if os.path.isfile(old_instance.image.path):
                        os.remove(old_instance.image.path)
                        
        # Llama al método save de la clase base para guardar el objeto
        super(ImageModel, self).save(*args, **kwargs)

        # Procesa la imagen utilizando Pillow para comprimirla y mantener la proporción
        if self.image:
            img = Image.open(self.image.path)
            max_size = (500, 500)  # Tamaño máximo de la imagen
            img.thumbnail(max_size, Image.LANCZOS)  # Redimensiona la imagen manteniendo la proporción
            img.save(self.image.path, quality=90)  # Guarda la imagen con calidad del 90%

class Player(ImageModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    nickname = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='users/', blank=True)
    instagram = models.CharField(max_length=200, blank=True)
    whatsapp = models.CharField(max_length=20, blank=True)
    country = CountryField(null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    
    # def save(self, *args, **kwargs):
    #     # Llama al método save de la clase base para guardar el objeto
    #     super(Player, self).save(*args, **kwargs)

    #     # Procesa la imagen utilizando Pillow para comprimirla y mantener la proporción
    #     if self.image:
    #         img = Image.open(self.image.path)
    #         max_size = (300, 300)  # Tamaño máximo de la imagen
    #         img.thumbnail(max_size, Image.LANCZOS)  # Redimensiona la imagen manteniendo la proporción
    #         img.save(self.image.path, quality=90)  # Guarda la imagen con calidad del 90%
    
    def __str__(self):
        return f"{self.name} {self.last_name} - {self.nickname}"
    
class Game(ImageModel):
    STATUS_CHOICES = [
        ('sin_empezar', 'Sin Empezar'),
        ('en_proceso', 'En Proceso'),
        ('terminado', 'Terminado'),
    ]
    
    id_name = models.CharField(max_length=50, unique=True,default='#')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='games/', blank=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PlayerInGame(ImageModel):
    STATUS_CHOICES = [
        ('sin_estado', 'Sin estado'),
        ('en_juego', 'En juego'),
        ('eliminado', 'Eliminado'),
        ('abandono', 'Abandono'),
        ('ganador', 'Ganador')
    ]
    
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    details_status = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='players/', blank=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    @property
    def nickname(self):
        return self.player.nickname

    def __str__(self):
        return self.player.name + " - " + self.game.title

class Score(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    playerInGame = models.ForeignKey(PlayerInGame, on_delete=models.SET_NULL, blank=True, null=True)
    score = models.IntegerField()
    details = models.CharField(max_length=100, blank=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.player.nickname + " - " + str(self.score)

class Post(ImageModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title