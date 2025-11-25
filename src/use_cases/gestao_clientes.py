"""
Caso de Uso: Gestão de Clientes
-------------------------------
Responsabilidade: Orquestrar validações e solicitar salvamento.
"""

import re

from src.core.interfaces import RepositorioClienteInterface
from src.core.models import Cliente

# Regex para validar e-mail (Trazido do legado, mas isolado aqui)
REG_EMAIL = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"


class CadastradorCliente:
    def __init__(self, repositorio: RepositorioClienteInterface):
        # Injeção de Dependência: Recebemos quem salva, não criamos aqui.
        self.repositorio = repositorio

    def cadastrar(self, dados: dict) -> bool:
        """
        Recebe um dicionário bruto, valida e tenta salvar.
        """
        # 1. Validação de Campos
        if "email" not in dados or "nome" not in dados:
            print("[Erro] Faltou campo obrigatório (nome ou email).")
            return False

        # 2. Validação de Regra de Negócio (E-mail)
        if not re.match(REG_EMAIL, dados["email"]):
            print(
                f"[Aviso] Email inválido detectado: {dados['email']} (Mas processando conforme legado)"
            )
            # No legado ele aceitava mesmo assim, mantivemos o comportamento mas logamos o aviso.

        # 3. Criação da Entidade (Model)
        novo_cliente = Cliente(
            nome=dados["nome"], email=dados["email"], cnpj=dados.get("cnpj", "")
        )

        # 4. Persistência (Usa a Interface)
        sucesso = self.repositorio.salvar(novo_cliente)

        if sucesso:
            self._enviar_email_boas_vindas(novo_cliente.email)

        return sucesso

    def _enviar_email_boas_vindas(self, email: str):
        """Simulação de envio de e-mail (Privado, pois é detalhe interno)."""
        print(f"--- Enviando email de boas vindas para {email} ---")
