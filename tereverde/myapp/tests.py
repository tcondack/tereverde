import pytest
from app.models import Parque

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
