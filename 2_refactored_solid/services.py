"""
Módulo de Serviços
------------------
Este módulo contém a lógica de negócios do sistema, separada em classes
com responsabilidade única (SRP).
"""

from models import Pedido

# pylint: disable=too-few-public-methods


class CalculadoraDeImposto:
    """Responsável apenas pelo cálculo de valores."""

    def calcular_total(self, pedido: Pedido) -> float:
        """Calcula o total do pedido aplicando taxas se necessário."""
        total = 0.0
        for item in pedido.itens:
            if item.categoria == "extra":
                total += item.valor * 1.1  # Taxa de 10%
            else:
                total += item.valor
        return total


class NotificadorEmail:
    """Responsável apenas pelo envio de notificações."""

    def notificar_gerente(self, total: float):
        """Simula o envio de um e-mail para o gerente."""
        if total > 100:
            print(f"[EMAIL] Atenção Gerente: Pedido alto de R$ {total:.2f}")
        else:
            print(f"[LOG] Pedido processado: R$ {total:.2f}")


class RepositorioArquivo:
    """Responsável apenas por salvar dados (Simulação de DB)."""

    def salvar_pedido(self, total: float):
        """Simula o salvamento do pedido em um banco de dados."""
        print(f"[DB] Salvando pedido no banco... Valor: {total}")
