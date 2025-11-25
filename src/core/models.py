"""
Módulo de Modelos (Entidades)
-----------------------------
Responsabilidade (SRP): Apenas definir a estrutura dos dados do domínio.
Não deve conter regras de negócio complexas ou acesso a banco de dados.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Cliente:
    """Representa um cliente da PetroBahia."""

    nome: str
    email: str
    cnpj: str


@dataclass
class Pedido:
    """Representa um pedido de compra de combustível."""

    cliente_nome: str
    produto: str
    quantidade: float
    cupom: Optional[str] = None
