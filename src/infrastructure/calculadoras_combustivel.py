"""
Implementação de Infraestrutura: Calculadoras de Combustível
------------------------------------------------------------
Pattern: Strategy
Responsabilidade: Implementar a matemática específica de cada produto.
Implementa: CalculadoraCombustivelInterface
"""

from src.core.interfaces import CalculadoraCombustivelInterface

# Preços base definidos como constantes (Evita Magic Numbers)
BASE_DIESEL = 3.99
BASE_GASOLINA = 5.19
BASE_ETANOL = 3.59
BASE_LUBRIFICANTE = 25.0


class CalculadoraDiesel(CalculadoraCombustivelInterface):
    def calcular_preco_base(self, quantidade: float) -> float:
        preco = BASE_DIESEL * quantidade
        # Regra de faixas de desconto do Diesel
        if quantidade > 1000:
            return preco * 0.90  # 10% off
        if quantidade > 500:
            return preco * 0.95  # 5% off
        return preco


class CalculadoraGasolina(CalculadoraCombustivelInterface):
    def calcular_preco_base(self, quantidade: float) -> float:
        preco = BASE_GASOLINA * quantidade
        # Regra de desconto fixo da Gasolina
        if quantidade > 200:
            return preco - 100.0
        return preco


class CalculadoraEtanol(CalculadoraCombustivelInterface):
    def calcular_preco_base(self, quantidade: float) -> float:
        preco = BASE_ETANOL * quantidade
        # Regra de desconto do Etanol
        if quantidade > 80:
            return preco * 0.97  # 3% off
        return preco


class CalculadoraLubrificante(CalculadoraCombustivelInterface):
    def calcular_preco_base(self, quantidade: float) -> float:
        # Refatoração: Trocamos o loop 'for' ineficiente por multiplicação simples
        return BASE_LUBRIFICANTE * quantidade
