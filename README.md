# 🛒 Sistema de Processamento de Pedidos (E-commerce)

Este projeto simula o backend de um sistema de vendas online. Ele é responsável por receber uma lista de itens, aplicar regras de impostos baseadas na categoria do produto e executar ações pós-venda (notificação e salvamento).

O projeto foi desenvolvido em duas versões ("Legado" vs "Refatorado") para demonstrar como boas práticas de engenharia tornam a lógica de negócios mais segura e clara.

---

## ⚙️ Funcionalidades e Regras de Negócio

O sistema implementa a seguinte lógica comercial:

### 1. Cálculo de Preço com Impostos
O sistema processa itens de diferentes categorias. A regra de taxação é:
* **Itens Normais:** O valor é somado integralmente.
* **Itens Extras (Luxo/Especiais):** Recebem uma taxa de **10%** sobre o valor original.
    * *Exemplo:* Um item "Mouse" de R$ 60,00 viraria R$ 66,00.

### 2. Sistema de Notificação Inteligente
Após calcular o total, o sistema decide quem avisar baseada no valor da compra:
* **Pedidos acima de R$ 100,00:** Envia um **Alerta Prioritário** para o Gerente (simulado via log).
* **Pedidos abaixo de R$ 100,00:** Apenas registra um log comum de operação.

### 3. Persistência de Dados
Todos os pedidos processados são enviados para um módulo de repositório que simula o salvamento em banco de dados ou arquivo de log.

---

## 📂 Arquitetura do Projeto

O código foi reestruturado seguindo o padrão de **Camadas (Layered Architecture)** para isolar essas regras:

### `models.py` (Dados)
Define O QUE é um "Item" e um "Pedido". Não faz contas, apenas transporta dados.

### `services.py` (O Cérebro)
Aqui vivem as regras de negócio descritas acima:
* `CalculadoraDeImposto`: Contém a lógica matemática dos 10%.
* `NotificadorEmail`: Contém a lógica do `if total > 100`.

### `main.py` (O Maestro)
Apenas cria os dados de teste e chama os serviços na ordem correta.

---

## 🛠 Ferramentas de Qualidade

Para garantir que essas regras de negócio não quebrem e o código permaneça legível, utilizamos:

| Ferramenta | Função |
| :--- | :--- |
| **Pytest** | Garante que a matemática (10% de taxa) esteja sempre correta. |
| **Pylint** | Garante que o código não tenha erros de lógica ou variáveis soltas. |
| **Black/Isort** | Mantém a formatação visual padronizada. |

---

## 🚀 Como Rodar o Sistema

Certifique-se de ativar seu ambiente virtual (`venv`).

### 1. Instalar Dependências
```powershell
pip install -r requirements.txt

---

## 📂 Estrutura do Projeto

O repositório está dividido em dois cenários para comparação ("Antes e Depois"):

```text
projeto-code-quality/
│
├── 📁 1_legacy_chaos/         # CENÁRIO 1: O Problema
│   └── processador.py         # Código "espaguete", sem padrão e difícil de manter.
│
├── 📁 2_refactored_solid/     # CENÁRIO 2: A Solução
│   ├── main.py                # Entrada do sistema (Orquestrador)
│   ├── models.py              # Definição de Dados (Data Classes)
│   └── services.py            # Regras de Negócio (Lógica Pura)
│
├── 📁 tests/                  # GARANTIA DE QUALIDADE
│   └── test_calculadora.py    # Testes unitários com Pytest
│
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação.