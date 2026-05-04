# Python-Currency-Tracker 
##  Instalação e Execução

1.  Clone este repositório:
    ```bash
    git clone https://github.com/VictorCunha1703/Python-Currency-Tracker
    ```
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3.  Execute o script:
    ```bash
    python scraper_cotacao.py
    ```

##  Estrutura do Log

O sistema gera um arquivo chamado `Log_financeiro.txt` na raizUm **README.md** de nível sênior não apenas explica o que o código faz, mas demonstra preocupação com a facilidade de instalação, manutenção e arquitetura. Ele deve vender o projeto como uma solução profissional e pronta para produção.

Aqui está o conteúdo do seu README formatado em Markdown:

---

#  Currency Tracker - Financial Automation

![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Stability](https://img.shields.io/badge/stability-stable-brightgreen.svg)

**Currency Tracker** é uma solução leve e robusta para monitoramento automatizado da cotação USD/BRL. O projeto foi desenvolvido com foco em modularidade e persistência de dados, utilizando a API do Yahoo Finance para extração de dados em tempo real.

##  Funcionalidades

*   **Extração via Yahoo Finance:** Consumo de dados financeiros atualizados.
*   **Gestão de Caminhos Dinâmicos:** Localização automática do diretório do script para gravação de logs (zero configuração de caminhos manuais).
*   **Persistência de Dados:** Registro histórico em arquivo `.txt` com timestamp formatado.
*   **Arquitetura Orientada a Objetos:** Código estruturado em classes para facilitar a manutenção e escalabilidade.
*   **Logging e Tratamento de Exceções:** Sistema resiliente contra falhas de conexão e timeouts de API.

##  Stack Tecnológica

*   **Linguagem:** Python 3.12
*   **Bibliotecas:**
    *   `yfinance`: Interface de comunicação com o Yahoo Finance.
    *   `os`: Manipulação de caminhos e sistema de arquivos.
    *   `datetime`: Gestão de temporalidade para registros de log.

##  Pré-requisitos

Antes de iniciar, certifique-se de ter o Python 3.12 instalado e um ambiente virtual configurado.
```bash
# Criação do ambiente virtual
python -m venv .venv

# Ativação do ambiente (Windows)
.\.venv\Scripts\activate
 Instalação e Execução
Clone este repositório:

Bash
git clone [https://github.com/seu-usuario/currency-tracker.git](https://github.com/seu-usuario/currency-tracker.git)
Instale as dependências:

Bash
pip install -r requirements.txt
Execute o script:

Bash
python scraper_cotacao.py
 Estrutura do Log
O sistema gera um arquivo chamado Log_financeiro.txt na raiz do projeto. Cada entrada segue o padrão abaixo:

DD/MM/AAAA HH:MM:SS | Dólar: R$ X.XXXX

 Arquitetura do Código
O projeto segue o princípio da Responsabilidade Única (SRP):

fetch_rate: Responsável exclusivamente pela comunicação externa.

save_log: Gerencia a lógica de I/O de arquivos e persistência.

main: Orquestra o fluxo de execução e fornece feedback ao usuário via console.

 
 Victor Cunha Desenvolvedor e Analista de Suporte (https://www.linkedin.com/in/victor-cunha-7ba715213/)
