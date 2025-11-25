from django.db import models
from multiselectfield import MultiSelectField

dia_semana = [
        ('Segunda-feira', 'Segunda-feira'),
        ('Terça-feira', 'Terça-feira'),
        ('Quarta-feira', 'Quarta-feira'),
        ('Quinta-feira', 'Quinta-feira'),
        ('Sexta-feira', 'Sexta-feira'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
        ]

class Parque(models.Model):
    nome =models.CharField(max_length=120)
    descricao = models.TextField()
    localizacao = models.TextField()
    horario_funcionamento = models.CharField(max_length=100)
    taxa_entrada = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    imagem = models.ImageField(upload_to='parques/', null=True, blank=True)
    dias_aberto = MultiSelectField(
    choices=dia_semana,
    default=[],
    blank=True)
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.nome

class Trilhas(models.Model):
    parque = models.ForeignKey(Parque, on_delete=models.CASCADE)
    nome = models.CharField(max_length=120)
    descricao = models.TextField()
    dificuldade = models.CharField(max_length=30, choices=[('Fácil', 'Fácil'), ('Médio', 'Médio'), ('Difícil', 'Difícil')])
    distancia = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to='trilhas/', null=True, blank=True)
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.nome

class Eventos(models.Model):
    parque = models.ForeignKey(Parque, on_delete=models.CASCADE)
    nome = models.CharField(max_length=120)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    preco = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    imagem = models.ImageField(upload_to='eventos/', null=True, blank=True)
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.nome


class Novidades(models.Model):
    parque = models.ForeignKey(Parque, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.parque.nome} - {self.titulo}"