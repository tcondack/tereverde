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

