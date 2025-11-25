"""
Implementação de Infraestrutura: Repositório TXT
------------------------------------------------
Responsabilidade: Gravar dados fisicamente em um arquivo de texto.
Implementa: RepositorioClienteInterface (DIP)
"""


from src.core.interfaces import RepositorioClienteInterface
from src.core.models import Cliente


class RepositorioClienteTXT(RepositorioClienteInterface):
    """Grava clientes no arquivo 'clientes.txt'."""

    def __init__(self, caminho_arquivo: str = "clientes.txt"):
        self.caminho = caminho_arquivo

    def salvar(self, cliente: Cliente) -> bool:
        """
        Escreve o dicionário do cliente no arquivo.
        Retorna True se sucesso, False se erro de IO.
        """
        try:
            # Simula o formato do legado: dicionário convertido para string
            linha = f"{{'nome': '{cliente.nome}', 'email': '{cliente.email}', 'cnpj': '{cliente.cnpj}'}}\n"

            # encoding='utf-8' resolve problemas de acentuação
            with open(self.caminho, "a", encoding="utf-8") as arquivo:
                arquivo.write(linha)
            return True
        except IOError as erro:
            print(f"Erro ao salvar no disco: {erro}")
            return False
