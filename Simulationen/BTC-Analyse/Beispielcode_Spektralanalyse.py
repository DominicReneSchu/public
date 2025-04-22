import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Lade Bitcoin-Daten (Daten von Januar 2021 bis Januar 2022)
btc = yf.download("BTC-USD", start="2021-01-01", end="2022-01-01")

# Extrahiere die Schlusskurse und Zeitstempel
prices = btc['Close']
timestamps = btc.index  # Zeitstempel der Daten

# Berechnung der Fourier-Transformation der Bitcoin-Daten
n = len(prices)
T = 1.0  # Zeitintervall (Tage)
x = np.linspace(0.0, n*T, n, endpoint=False)  # Zeitachse für Fourier-Transformation
yf = np.fft.fft(prices)  # Fourier-Transformation
xf = np.fft.fftfreq(n, T)  # Frequenzen
y_plot = np.abs(yf)  # Betrag der Fourier-Transformation

# Resonanzmodell erstellen (z.B. einfache Oszillation)
A = 1.0  # Amplitude
omega = 2 * np.pi / 365  # Frequenz (1 Jahr, tägliche Schritte)
phi = 0  # Phase
resonance_curve = A * np.sin(omega * x + phi)

# Erstelle das Diagramm
plt.figure(figsize=(10, 6))

# Plot der Spektralanalyse der Bitcoin-Kurse
plt.plot(xf[:n//2], y_plot[:n//2], label="Spektralanalyse", color='blue')
plt.title('Spektralanalyse und Resonanzmodell für Bitcoin')
plt.xlabel('Frequenz (Hz)')
plt.ylabel('Amplitude')

# Überlagere das Resonanzmodell auf das Diagramm
plt.plot(timestamps, resonance_curve[:len(timestamps)], label="Resonanzmodell", linestyle='--', color='red')
plt.legend()

# Kein Preisdiagramm anzeigen
plt.grid(True)

# Zeige das Diagramm an
plt.show()
