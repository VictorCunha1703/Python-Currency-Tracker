import yfinance as yf
from datetime import datetime


def buscar_cotacao_profissional():
    try:

        ticker = yf.Ticker("USDBRL=X")


        dados = ticker.history(period="1d")

        if not dados.empty:
            preco_atual = dados['Close'].iloc[-1]
            return round(preco_atual, 4)
        else:
            return "Dados não encontrados"

    except Exception as e:
        return f"Erro na captura: {e}"



cotacao = buscar_cotacao_profissional()
data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

if isinstance(cotacao, float):
    print(f"✅ Sucesso! Dólar hoje: R$ {cotacao}")


    log = f"{data_hora} | Dólar: R$ {cotacao}\n"
    with open("log_financeiro.txt", "a", encoding="utf-8") as f:
        f.write(log)
    print("Dados registrados no 'log_financeiro.txt'")
else:
    print(f"❌ Erro: {cotacao}")
