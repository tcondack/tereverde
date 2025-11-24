from django.contrib import admin
from myapp.models import Parque, Trilhas, Eventos, Novidades

@admin.register(Parque)
class ParqueAdmin(admin.ModelAdmin):
    list_display = ('nome', 'localizacao', 'horario_funcionamento', 'taxa_entrada')
    search_fields = ('nome', 'localizacao')

@admin.register(Trilhas)
class TrilhasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'parque_id', 'dificuldade', 'distancia')
    search_fields = ('nome',)
    list_filter = ('dificuldade',)

@admin.register(Eventos)
class EventosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'parque_id', 'data_inicio', 'data_fim', 'preco')
    search_fields = ('nome',)
    list_filter = ('data_inicio', 'data_fim')

@admin.register(Novidades)
class NovidadesAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    search_fields = ('titulo',)
    list_filter = ('data_publicacao',)