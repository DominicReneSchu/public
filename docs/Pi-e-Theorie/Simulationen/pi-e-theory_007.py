import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Parameter
pi = np.pi
e = np.e

# Frequenz und Masse als Parameter
mass = 1.0   # Masse des Systems
frequency = 1.0  # Frequenz der Schwingung

# Zeitparameter
t = np.linspace(0, 10, 500)

# Bewusstseinsfaktor alpha (Wert zwischen 0 und 1)
alpha = 0.5

# Schwingungsfunktionen mit Masse und Frequenz
def resonance(t, alpha, mass, frequency):
    try:
        # Berechnung der Resonanz zwischen pi und e mit Frequenz und Masse
        pi_wave = np.sin(2 * np.pi * frequency * t)
        e_wave = np.cos(2 * np.pi * frequency * t)

        # Modifikation der Schwingungen durch Masse und Alpha
        resonance_signal = alpha * e_wave + (1 - alpha) * pi_wave
        energy = mass * np.power(resonance_signal, 2)  # Energiefluss ist proportional zur Masse und Amplitude der Schwingung

        if np.any(energy <= 0):  # Fehlerbehandlung, falls Energie negativ oder null wird
            raise ValueError("Energie darf nicht null oder negativ sein!")
        
        return resonance_signal, energy

    except Exception as e:
        # Fehler in die log.txt schreiben
        with open("log.txt", "a") as log_file:
            log_file.write(f"Fehler: {str(e)}\n")
        raise e  # Fehler erneut auslösen

# Berechnung der Schwingungen und Energie
try:
    resonance_signal, energy = resonance(t, alpha, mass, frequency)
    # Entropie basierend auf Energie
    entropy = np.log(energy + 1)  # Entropie als logarithmische Funktion der Energie

    # Log-Datei schreiben
    with open("log.txt", "a") as log_file:
        log_file.write(f"Parameter:\nMass: {mass}\nFrequency: {frequency}\nAlpha: {alpha}\n\n")
        log_file.write(f"Berechnungen:\nEnergie: {energy[:10]}...\nEntropie: {entropy[:10]}...\n")  # Ausgabe der ersten 10 Werte

except Exception as e:
    # Fehlerfall in log.txt
    with open("log.txt", "a") as log_file:
        log_file.write(f"Fehler bei Berechnungen: {str(e)}\n")

# 3D-Darstellung
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Erstellen eines regelmäßigen Gitters für X und Y
X, Y = np.meshgrid(t, np.full_like(t, alpha))  # Erstelle ein Meshgrid aus Zeit t und Alpha

# Z-Achse: Entropie als 2D-Matrix
Z = np.tile(np.log(energy + 1), (len(t), 1))  # Entropie wird als 2D-Matrix erstellt

# Verwenden von plot_surface anstelle von plot_trisurf
ax.plot_surface(X, Y, Z.T, cmap='inferno', edgecolor='none')  # Z.T, um Z korrekt auszurichten

# Beschriftung der Achsen
ax.set_xlabel('Zeit (t)')
ax.set_ylabel('Bewusstseinsfaktor Alpha')
ax.set_zlabel('Entropie')

# Titel
ax.set_title('Resonanz und Entropie im System (Masse und Frequenz integriert)')

# Anzeigen der Grafik
plt.show()
