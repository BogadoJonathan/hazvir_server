from rest_framework import serializers
from .models import Votacion, VotoDelPublico

class VotacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votacion
        fields = '__all__'

class VotoDelPublicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotoDelPublico
        fields = '__all__'