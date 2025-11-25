"""
Módulo de Interfaces (Contratos)
--------------------------------
Responsabilidade (DIP/ISP): Definir contratos abstratos para que o sistema
dependa de abstrações, e não de implementações concretas.
"""

from abc import ABC, abstractmethod

from src.core.models import Cliente

# --- Contratos para Persistência (Banco de Dados/Arquivo) ---


class RepositorioClienteInterface(ABC):
    """Contrato para quem quiser salvar/ler clientes (ISP: focado em clientes)."""

    @abstractmethod
    def salvar(self, cliente: Cliente) -> bool:
        """Deve salvar o cliente e retornar True se sucesso."""
        raise NotImplementedError


# --- Contratos para Regras de Negócio (Estratégias de Preço) ---


class CalculadoraCombustivelInterface(ABC):
    """
    Pattern: Strategy
    Contrato para cálculo de preço base (OCP: novos combustíveis implementam isso).
    """

    @abstractmethod
    def calcular_preco_base(self, quantidade: float) -> float:
        """Recebe a quantidade e retorna o preço bruto."""
        raise NotImplementedError


class DescontoStrategyInterface(ABC):
    """
    Pattern: Strategy
    Contrato para aplicação de descontos/cupons (OCP: novos cupons implementam isso).
    """

    @abstractmethod
    def aplicar_desconto(self, valor_bruto: float, produto: str) -> float:
        """Recebe o valor e aplica a regra do desconto."""
        raise NotImplementedError
