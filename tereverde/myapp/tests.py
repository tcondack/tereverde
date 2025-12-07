from django.test import TestCase
from myapp.models import Parque, Trilhas, Eventos, Novidades
from django.utils import timezone


class ParqueModelTest(TestCase):
    def setUp(self):
        data_inicio = timezone.now()
        data_fim = timezone.now()

        self.parque = Parque.objects.create(
            nome="Parque Teste",
            descricao="Descrição do parque teste",  
            localizacao="Localização do parque teste",
            horario_funcionamento="08:00 - 18:00",
            ativo=True,

        )

        self.trilha = Trilhas.objects.create(
            parque=self.parque,
            nome="Trilha Teste",
            descricao="Descrição da trilha",
            dificuldade="Fácil",
            distancia=4.2,
            ativo=True,
        )

        self.evento = Eventos.objects.create(
            parque=self.parque,
            nome="Evento Teste",
            descricao="Descrição do evento",
            data_inicio=data_inicio,
            data_fim=data_fim,
            ativo=True,
        )

    def test_parque_creation(self):
        self.assertEqual(self.parque.nome, "Parque Teste")
        self.assertTrue(self.parque.ativo)

