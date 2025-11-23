"""
Módulo Principal (Entry Point)
------------------------------
Responsável por iniciar o sistema e conectar as camadas
(Injeção de Dependência Manual).
"""

from models import Item, Pedido
from services import CalculadoraDeImposto, NotificadorEmail, RepositorioArquivo


def executar_sistema():
    """
    Função principal que orquestra o fluxo:
    Cria dados -> Instancia serviços -> Executa lógica.
    """
    # 1. Preparação dos Dados (Models)
    itens = [
        Item(nome="Livro", valor=50.0, categoria="normal"),
        Item(nome="Mouse", valor=60.0, categoria="extra"),
    ]
    pedido = Pedido(itens=itens)

    # 2. Instanciação dos Serviços (Dependency Injection)
    calculadora = CalculadoraDeImposto()
    notificador = NotificadorEmail()
    repositorio = RepositorioArquivo()

    # 3. Execução Lógica
    total = calculadora.calcular_total(pedido)

    notificador.notificar_gerente(total)
    repositorio.salvar_pedido(total)


if __name__ == "__main__":
    executar_sistema()
