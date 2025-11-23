"""
Módulo de Modelos
-----------------
Define as estruturas de dados (Data Classes) usadas no sistema.
Não contém regras de negócio, apenas definições.
"""

from dataclasses import dataclass


@dataclass
class Item:
    """Representa um produto individual no sistema."""

    nome: str
    valor: float
    categoria: str


@dataclass
class Pedido:
    """Representa um conjunto de itens comprados."""

    itens: list[Item]
