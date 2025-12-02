from rest_framework import serializers
from .models import Parque, Trilhas, Eventos

class ParqueSerializer(serializers.ModelSerializer):
  """ Serializer para o modelo Parque"""
  class Meta:
    model = Parque
    fields = '__all__'

class TrilhasSerializer(serializers.ModelSerializer):
  """ Serializer para o modelo Trilhas"""
  class Meta:
    model = Trilhas
    fields = '__all__'

class EventosSerializer(serializers.ModelSerializer):
  """ Serializer para o modelo Eventos"""
  class Meta:
    model = Eventos
    fields = '__all__'
