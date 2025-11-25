import pytest
import sys
import os

# 1. Ajuste de Caminho (Path Hacking)
# Isso garante que o teste consiga enxergar a pasta 'src' que está na raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.models import Cliente
from src.core.interfaces import RepositorioClienteInterface
from src.use_cases.gestao_clientes import CadastradorCliente
from src.infrastructure.calculadoras_combustivel import CalculadoraDiesel, CalculadoraGasolina

# --- O QUE O PYTEST FAZ AQUI? ---

# CENÁRIO 1: Teste de Unidade (Matemática Pura)
# Estamos testando se a lógica da CalculadoraDiesel está respeitando a regra dos 10%
def test_calculo_diesel_com_desconto():
    calc = CalculadoraDiesel()
    # 1200 litros * 3.99 = 4788.0
    # Regra: Acima de 1000L ganha 10% de desconto (x 0.90) -> Esperado: 4309.2
    resultado = calc.calcular_preco_base(1200)
    
    # O assert verifica se a conta bateu. Se der diferente, o teste explode (FAIL).
    assert abs(resultado - 4309.2) < 0.01

# CENÁRIO 2: Teste de Arquitetura (O Pulo do Gato - Mock)
# Aqui criamos um "Repositório Falso" em memória.
# O objetivo é provar que o sistema NÃO depende do arquivo 'clientes.txt'.

class RepositorioFake(RepositorioClienteInterface):
    def __init__(self):
        self.banco_de_dados_fake = []

    def salvar(self, cliente: Cliente) -> bool:
        self.banco_de_dados_fake.append(cliente)
        return True

def test_cadastro_cliente_sem_criar_arquivo_txt():
    # Arrange (Preparação)
    repo_falso = RepositorioFake()
    cadastrador = CadastradorCliente(repositorio=repo_falso)
    dados = {"nome": "Tester", "email": "teste@petro.com", "cnpj": "000"}

    # Act (Ação)
    sucesso = cadastrador.cadastrar(dados)

    # Assert (Verificação)
    assert sucesso is True
    assert len(repo_falso.banco_de_dados_fake) == 1
    print("\nSucesso! O teste rodou sem criar nenhum arquivo no Windows.")