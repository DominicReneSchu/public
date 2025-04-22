import yfinance as yf
import matplotlib.pyplot as plt

# Lade Bitcoin-Daten
btc_data = yf.download('BTC-USD', start='2015-01-01', end='2023-12-31')

# Visualisierung des Bitcoin-Preises
plt.figure(figsize=(10, 6))
plt.plot(btc_data['Close'], label="Bitcoin Preis")
plt.title('Bitcoin Preis Entwicklung')
plt.xlabel('Datum')
plt.ylabel('Preis in USD')
plt.legend()

# Zeige die Plot
plt.show()

# Fenster offen halten
input("Drücke Enter, um das Fenster zu schließen...")
