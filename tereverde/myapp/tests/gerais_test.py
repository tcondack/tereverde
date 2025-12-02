from django.test import TestCase
from myapp.models import Parque, Trilhas, Eventos, Novidades

class ParqueModelTest(TestCase):
    def setUp(self):
        self.parque = Parque.objects.create(
            nome="Parque Teste",
            descricao="Descrição do parque teste",  
            Localuizacao="Localização do parque teste",
            horario_funcionamento="08:00 - 18:00",
            ativo=True,

        )

class TrilhasModelTest(TestCase):
	def setUp(self):
		self.trilha = Trilhas.objects.create(
		nome="trilha teste",
		localizacao ="teresópolis",
		horario_funcionamento="08:00",
	)

class EventosModelTest(TestCase):
	def setUp(self):
		self.eventos = Eventos.object.create(
		nome="FEsta no parque",
		decricao="Sejam todos bem-vindos ao nosso parque...",
		data_inicio="15-12-2025",
		data_fim="19-12-2025",
	)

