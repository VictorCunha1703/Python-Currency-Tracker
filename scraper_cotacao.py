import yfinance as yf
from datetime import datetime
from typing import Union, Optional
import os

class CurrencyTracker:
    def __init__(self, ticker_symbol: str = "USDBRL=X"):
        self.ticker_symbol = ticker_symbol
        self.ticker = yf.Ticker(self.ticker_symbol)
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.log_file = os.path.join(self.base_path, "Log_financeiro.txt")

    def fetch_rate(self) -> Optional[float]:
        try:
            data = self.ticker.history(period="1d")
            if not data.empty:
                price = data['Close'].iloc[-1]
                return round(float(price), 4)
            return None
        except Exception:
            return None

    def save_log(self, value: float) -> None:
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        log_entry = f"{timestamp} | Dólar: R$ {value}\n"
        
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry)

def main():
    tracker = CurrencyTracker()
    value = tracker.fetch_rate()

    if value:
        print(f"✅ Valor capturado: R$ {value}")
        tracker.save_log(value)
        print(f"📂 Registrado em: {tracker.log_file}")
    else:
        print("❌ Falha ao obter cotação. Verifique a conexão ou o ticker.")

if __name__ == "__main__":
    main()