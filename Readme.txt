markdown
# Python Currency Tracker 

Este é um script de automação focado em coleta de dados financeiros estáveis. O objetivo principal foi criar um monitor de câmbio que não quebrasse com mudanças simples no HTML dos sites de busca.

##  Por que usei yfinance e não Requests puro?
No início do desenvolvimento, utilizei a biblioteca `requests` para fazer scraping direto de portais de notícias. Porém, devido às constantes mudanças de classes CSS e bloqueios de bot, optei por migrar para o `yfinance`. 
Essa escolha garante que o projeto utilize uma fonte de dados estruturada (via API do Yahoo Finance), tornando a automação muito mais confiável para uso em produção.

##  O que o script faz:
- Consulta o par de moedas USD/BRL (Dólar Comercial).
- Trata erros de conexão e retornos vazios para evitar crash do sistema.
- Gera um arquivo de log (`historico_cotacoes.txt`) para auditoria posterior dos valores.

## Requisitos
- Python 3.8+
- Bibliotecas: `yfinance` e `pandas` (instale via pip)

```bash
pip install yfinance pandas


## Como rodar
Basta executar o arquivo principal:
bash
python Scraper_cotacao



Projeto prático para estudo de automação e manipulação de dados com Python.
