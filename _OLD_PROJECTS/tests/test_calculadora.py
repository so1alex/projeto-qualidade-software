import pytest
import sys
import os

# Ajuste técnico para o teste encontrar a pasta '2_refactored_solid'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../2_refactored_solid')))

from models import Item, Pedido
from services import CalculadoraDeImposto

# --- FIXTURES (SOLID: Injeção de Dependência nos Testes) ---
@pytest.fixture
def calculadora():
    return CalculadoraDeImposto()

@pytest.fixture
def pedido_misto():
    return Pedido(itens=[
        Item(nome="A", valor=100, categoria="normal"), # 100
        Item(nome="B", valor=100, categoria="extra")   # 110 (10% taxa)
    ])

# --- TESTES (Clean Code: Claros e Diretos) ---
def test_calculo_total_com_taxa(calculadora, pedido_misto):
    resultado = calculadora.calcular_total(pedido_misto)
    assert resultado == 210.0

def test_calculo_lista_vazia(calculadora):
    pedido_vazio = Pedido(itens=[])
    assert calculadora.calcular_total(pedido_vazio) == 0.0