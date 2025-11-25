"""
Caso de Uso: Processamento de Pedidos
-------------------------------------
Responsabilidade: Calcular preço final combinando estratégias de
combustível e desconto.
"""

from src.core.interfaces import CalculadoraCombustivelInterface
from src.core.models import Pedido


class ProcessadorDePedidos:
    def __init__(self, calculadoras: dict, descontos: dict):
        """
        Recebe os mapas de estratégias (Injeção de Dependência).
        Ex: calculadoras = {'diesel': CalculadoraDiesel(), ...}
        """
        self.calculadoras = calculadoras
        self.descontos = descontos

    def processar(self, pedido: Pedido) -> float:
        """Executa o fluxo completo de precificação."""

        # 1. Validação Básica
        if pedido.quantidade == 0:
            print("Quantidade zero, retornando 0.")
            return 0.0

        # 2. Seleção da Estratégia de Combustível (Factory simplificada)
        calculadora: CalculadoraCombustivelInterface = self.calculadoras.get(
            pedido.produto
        )

        if not calculadora:
            print(f"Produto desconhecido: {pedido.produto}. Retornando 0.")
            return 0.0

        # 3. Cálculo do Preço Base
        preco = calculadora.calcular_preco_base(pedido.quantidade)

        # Tratamento de erro legado (preço negativo)
        if preco < 0:
            print("Erro crítico: Preço negativo. Ajustando para 0.")
            preco = 0.0

        # 4. Seleção e Aplicação do Desconto
        # Se o cupom não existir no mapa, usa a estratégia 'SemDesconto' (None -> SemDesconto)
        estrategia_desconto = self.descontos.get(pedido.cupom, self.descontos[None])
        preco_final = estrategia_desconto.aplicar_desconto(preco, pedido.produto)

        # 5. Formatação Final (Regras de arredondamento do legado)
        preco_formatado = self._aplicar_arredondamento_legado(
            preco_final, pedido.produto
        )

        print(
            f"Pedido OK: {pedido.cliente_nome} | {pedido.produto} | Qtd: {pedido.quantidade} => R$ {preco_formatado}"
        )
        return preco_formatado

    def _aplicar_arredondamento_legado(self, valor: float, produto: str) -> float:
        """Encapsula a lógica estranha de arredondamento do sistema antigo."""
        if produto == "diesel":
            return round(valor, 0)
        elif produto == "gasolina":
            return round(valor, 2)
        else:
            # Lógica de truncar duas casas decimais manualmente (do legado)
            return float(int(valor * 100) / 100.0)
