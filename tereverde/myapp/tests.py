import pytest
from app.models import Parque, Trilhas, Eventos

@pytest.fixture
def parque():
    return Parque.objects.create(
        nome="Parque Central",
        descricao="Um parque muito bonito",
        localizacao="Vieira",
        taxa_entrada=0,01,
        horario_funcionamento="08:00 - 14:00",
        dia_semana="sexta-feira",
    )

@pytest.fixture
def trilhas ()
    return Trilhas.objects-create(
    nome="Trilha do Sino",
    descricao ="Uma Trilha sensacional, com muitas belezas e uma longa caminhada",
    dificuldade="Dificil",
    distancia="9,55",
    )

@pytest.fixture
def Eventos()
    return Eventos.objects.create(
    nome="Caminhada pelo parque",
    descricao="Caminhada pelo Parque municipal Montanhas de Teresópolis",
    conteudo="Venha desfrutar da mais bela caminhada da região",
    data_publicacao="15-10-2025",
    )
