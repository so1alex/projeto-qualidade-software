"""
Ponto de Entrada (Entry Point) - PetroBahia
-------------------------------------------
Responsabilidade: Configurar a Injeção de Dependência e iniciar o sistema.
"""

from src.core.models import Pedido
from src.infrastructure.calculadoras_combustivel import (
    CalculadoraDiesel,
    CalculadoraEtanol,
    CalculadoraGasolina,
    CalculadoraLubrificante,
)
from src.infrastructure.descontos import (
    DescontoLub2,
    DescontoMega10,
    DescontoNovo5,
    SemDesconto,
)
from src.infrastructure.repositorio_txt import RepositorioClienteTXT
from src.use_cases.gestao_clientes import CadastradorCliente
from src.use_cases.processador_pedidos import ProcessadorDePedidos


def executar_sistema():
    print("==== Início processamento PetroBahia (Refatorado) ====")

    # --- 1. Configuração da Injeção de Dependência (Container) ---

    # Preparando o repositório (Infrastructure)
    repo_txt = RepositorioClienteTXT("clientes_refatorado.txt")

    # Preparando os mapas de estratégia (Combustíveis)
    mapa_calculadoras = {
        "diesel": CalculadoraDiesel(),
        "gasolina": CalculadoraGasolina(),
        "etanol": CalculadoraEtanol(),
        "lubrificante": CalculadoraLubrificante(),
    }

    # Preparando os mapas de estratégia (Cupons)
    mapa_descontos = {
        "MEGA10": DescontoMega10(),
        "NOVO5": DescontoNovo5(),
        "LUB2": DescontoLub2(),
        None: SemDesconto(),  # Caso padrão (Null Object Pattern)
    }

    # Instanciando os Casos de Uso com as dependências
    cadastrador = CadastradorCliente(repositorio=repo_txt)
    processador = ProcessadorDePedidos(
        calculadoras=mapa_calculadoras, descontos=mapa_descontos
    )

    # --- 2. Execução: Cadastro de Clientes ---
    dados_clientes = [
        {"nome": "Ana Paula", "email": "ana@@petrobahia", "cnpj": "123"},
        {"nome": "Carlos", "email": "carlos@petrobahia.com", "cnpj": "456"},
    ]

    for dados in dados_clientes:
        if cadastrador.cadastrar(dados):
            print(f"-> Cliente {dados['nome']} processado com sucesso.")
        else:
            print(f"-> Falha ao processar {dados['nome']}.")

    print("-" * 30)

    # --- 3. Execução: Processamento de Pedidos ---
    lista_pedidos_brutos = [
        {"cliente": "TransLog", "produto": "diesel", "qtd": 1200, "cupom": "MEGA10"},
        {"cliente": "MoveMais", "produto": "gasolina", "qtd": 300, "cupom": None},
        {"cliente": "EcoFrota", "produto": "etanol", "qtd": 50, "cupom": "NOVO5"},
        {"cliente": "PetroPark", "produto": "lubrificante", "qtd": 12, "cupom": "LUB2"},
    ]

    valores_finais = []

    for p_dict in lista_pedidos_brutos:
        # Convertendo dict bruto para Objeto (Model)
        pedido = Pedido(
            cliente_nome=p_dict["cliente"],
            produto=p_dict["produto"],
            quantidade=p_dict["qtd"],
            cupom=p_dict["cupom"],
        )

        valor = processador.processar(pedido)
        valores_finais.append(valor)

    print("-" * 30)
    print(f"TOTAL GERAL = {sum(valores_finais):.2f}")
    print("==== Fim processamento PetroBahia ====")


if __name__ == "__main__":
    executar_sistema()
