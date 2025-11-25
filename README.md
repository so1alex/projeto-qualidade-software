# 🛢️ PetroBahia S.A. - Refatoração de Sistema Legado

Este projeto consiste na análise, diagnóstico e refatoração completa de um sistema legado de processamento de pedidos de combustíveis. 

O objetivo foi transformar um código procedural, acoplado e difícil de manter em uma arquitetura robusta, testável e aderente aos princípios **SOLID** e **Clean Architecture**.

---

## 🕵️‍♂️ Diagnóstico: Problemas Encontrados no Legado

Antes da refatoração, o código apresentava violações graves de boas práticas:

1.  **Violação do OCP (Open/Closed Principle):** * O cálculo de preços dependia de cadeias gigantes de `if/else` para verificar o tipo de combustível (`diesel`, `gasolina`, etc.). Para adicionar um novo produto, era necessário modificar o código principal, gerando risco de bugs.
2.  **Violação do SRP (Single Responsibility Principle):**
    * O módulo de clientes misturava validação de dados (CPF/Email), persistência (gravar em arquivo `.txt`) e notificação (prints de envio de email).
3.  **Violação do DIP (Dependency Inversion Principle):**
    * O sistema dependia diretamente de implementações concretas (leitura direta de disco rígido), tornando impossível a criação de testes unitários isolados.
4.  **Acoplamento e Rigidez:**
    * Regras de negócio (descontos) estavam misturadas com regras de apresentação (arredondamento de casas decimais).

---

## 🏗️ Decisões de Design e Arquitetura

Para resolver os problemas acima, adotou-se uma **Arquitetura Limpa (Layered Architecture)** dividida em 4 camadas:

### 1. Camada Core (`src/core`)
* **Responsabilidade:** Contém as Entidades (`models.py`) e os Contratos (`interfaces.py`).
* **Decisão:** Inverter a dependência. O sistema não depende mais de arquivos `.txt`, mas sim de uma interface `RepositorioClienteInterface`.

### 2. Camada Infrastructure (`src/infrastructure`)
* **Responsabilidade:** Implementar os detalhes técnicos (IO, Banco de Dados, Algoritmos Específicos).
* **Design Pattern (Strategy):** Para resolver o problema dos `if/else` de combustíveis e cupons, utilizou-se o padrão **Strategy**. Cada combustível (Diesel, Gasolina) agora é uma classe separada que implementa `CalculadoraCombustivelInterface`.
    * *Benefício:* Adicionar "Hidrogênio" no futuro não exige alterar o código existente, apenas criar uma nova classe.

### 3. Camada Use Cases (`src/use_cases`)
* **Responsabilidade:** Orquestrar as regras de negócio.
* **Decisão:** Separar a validação do cliente da persistência. O `CadastradorCliente` apenas coordena: ele pede para validar e depois pede para o repositório salvar.

### 4. Camada Main (`main.py`)
* **Responsabilidade:** Injeção de Dependência.
* **Decisão:** O `main.py` é o único ponto do sistema que conhece as implementações concretas (`RepositorioTXT`, `CalculadoraDiesel`). Ele "monta" o sistema e injeta as dependências nos casos de uso.

---

## 🛠️ Stack Tecnológica e Qualidade

O projeto garante a qualidade contínua através das ferramentas:

* **Pylint:** Nota **10.00/10** (Código limpo e sem "Code Smells").
* **Black & Isort:** Padronização visual estrita (PEP 8).
* **Pytest:** Testes unitários validando a lógica matemática e a arquitetura (DIP).

## 🚀 Como Executar

Certifique-se de estar com o ambiente virtual ativo.

### 1. Executar o Sistema
```powershell
python main.py