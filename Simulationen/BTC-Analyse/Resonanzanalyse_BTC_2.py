import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging
from pmdarima import auto_arima
from datetime import datetime

# Logger einrichten
logging.basicConfig(filename='btc_forecast.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Funktion, um den Logger zu testen
def log_test_message():
    logging.info("Logger gestartet - Beginn der Berechnungen.")

# Daten einlesen (hier musst du deinen DataFrame laden)
def load_data():
    # Beispiel: Lade historische Bitcoin-Daten als CSV-Datei
    # df = pd.read_csv('path_to_your_data.csv', parse_dates=['Date'], index_col='Date')
    # Beispielhafte Daten als Platzhalter
    dates = pd.date_range(start="2023-01-01", periods=500, freq="D")
    data = np.random.normal(20000, 5000, size=(500,))  # Platzhalter-Daten (Bitcoin-Preise)
    df = pd.DataFrame(data, index=dates, columns=["Close"])
    return df

# Vorhersage mit AutoARIMA
def predict_future(data, forecast_steps=30):
    """
    Erzeugt eine ARIMA-basierte Vorhersage für die zukünftigen Bitcoin-Kurse mit AutoARIMA.
    """
    logging.info("Starte Vorhersage der Bitcoin-Kurse mit AutoARIMA.")
    
    # AutoARIMA-Modell zur Bestimmung der besten Parameter (p, d, q)
    model = auto_arima(data['Close'], seasonal=False, stepwise=True, trace=True)

    # Vorhersage der nächsten 'forecast_steps' Tage
    forecast = model.predict(n_periods=forecast_steps)

    # Datumsreihe für die Vorhersage
    forecast_dates = pd.date_range(data.index[-1], periods=forecast_steps + 1, freq='D')[1:]

    return forecast, forecast_dates

# Vorhersage visualisieren
def plot_forecast(data, forecast, forecast_dates):
    """
    Plottet die historischen Bitcoin-Kurse sowie die Vorhersage.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label="Historische Bitcoin-Kurse")
    plt.plot(forecast_dates, forecast, label="Vorhergesagte Bitcoin-Kurse", linestyle='--')
    plt.title("Bitcoin-Preis Vorhersage")
    plt.xlabel("Datum")
    plt.ylabel("Preis in USD")
    plt.legend()
    plt.grid(True)
    plt.show()

# Hauptfunktion
def main():
    try:
        logging.info("Starte Bitcoin Vorhersage-Skript...")
        df = load_data()
        forecast_steps = 30  # Vorhersage für die nächsten 30 Tage
        forecast, forecast_dates = predict_future(df, forecast_steps)
        
        logging.info("Vorhersage abgeschlossen.")
        plot_forecast(df, forecast, forecast_dates)

    except Exception as e:
        logging.error(f"Fehler aufgetreten: {e}")

if __name__ == "__main__":
    main()
