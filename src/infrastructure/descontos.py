"""
Implementação de Infraestrutura: Estratégias de Desconto
--------------------------------------------------------
Pattern: Strategy
Responsabilidade: Aplicar regras de cupom sobre o valor.
Implementa: DescontoStrategyInterface
"""

from src.core.interfaces import DescontoStrategyInterface


class DescontoMega10(DescontoStrategyInterface):
    def aplicar_desconto(self, valor_bruto: float, produto: str) -> float:
        return valor_bruto * 0.90  # 10% off


class DescontoNovo5(DescontoStrategyInterface):
    def aplicar_desconto(self, valor_bruto: float, produto: str) -> float:
        return valor_bruto * 0.95  # 5% off


class DescontoLub2(DescontoStrategyInterface):
    def aplicar_desconto(self, valor_bruto: float, produto: str) -> float:
        # Regra específica do legado: Só aplica se for lubrificante
        if produto == "lubrificante":
            return valor_bruto - 2.0
        return valor_bruto


class SemDesconto(DescontoStrategyInterface):
    """Strategy Null Object: Usado quando não há cupom."""

    def aplicar_desconto(self, valor_bruto: float, produto: str) -> float:
        return valor_bruto
