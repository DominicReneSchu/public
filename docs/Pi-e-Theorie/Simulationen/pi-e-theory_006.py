import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import logging
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Fehlerprotokollierung einrichten
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Funktion zur Berechnung von Entropie und Energie mit Fehlerüberprüfung
def moving_average(data, window):
    try:
        return np.convolve(data, np.ones(window)/window, mode='same')
    except Exception as e:
        logging.error(f"Fehler bei der Berechnung des gleitenden Mittelwerts: {e}")
        raise

def compute(alpha):
    try:
        signal = signal_pi + alpha * signal_e
        energy = signal**2
        entropy = moving_average(energy, 50)
        return signal, energy, entropy
    except Exception as e:
        logging.error(f"Fehler bei der Berechnung von Signal, Energie und Entropie: {e}")
        raise

# Zeitachse
t = np.linspace(0, 10, 1000)

# Frequenzen
f_pi = np.pi
f_e = np.e

# Vorberechnung der Einzelsignale
signal_pi = np.sin(2 * np.pi * f_pi * t)
signal_e = np.sin(2 * np.pi * f_e * t)

# Initialer Bewusstseinsfaktor
alpha_init = 0.5

# Berechnungen für das initiale alpha
try:
    signal, energy, entropy = compute(alpha_init)
    logging.info(f"Berechnungen erfolgreich durchgeführt mit alpha = {alpha_init}")
except Exception as e:
    logging.error(f"Fehler bei den Anfangsberechnungen: {e}")

# 3D-Plot vorbereiten
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Zeit, Amplitude und Alpha-Achse
t_3d, alpha_3d = np.meshgrid(t, np.linspace(0, 1, 100))

# Berechnung der Z-Werte (Amplitude und Entropie für 3D)
try:
    z_signal = np.sin(2 * np.pi * f_pi * t_3d) + alpha_3d * np.sin(2 * np.pi * f_e * t_3d)
    z_entropy = moving_average(z_signal**2, 50)
    logging.info("3D-Daten erfolgreich berechnet.")
except Exception as e:
    logging.error(f"Fehler bei der 3D-Datenberechnung: {e}")

# 3D Oberflächenplot
try:
    ax.plot_surface(t_3d, alpha_3d, z_signal, cmap='viridis', edgecolor='none', alpha=0.7)
    ax.plot_surface(t_3d, alpha_3d, z_entropy, cmap='inferno', edgecolor='none', alpha=0.3)
    logging.info("3D-Plot erfolgreich erstellt.")
except Exception as e:
    logging.error(f"Fehler bei der Erstellung des 3D-Plots: {e}")

# Achsenbeschriftungen
ax.set_xlabel('Zeit (t)')
ax.set_ylabel('Bewusstseinsfaktor (α)')
ax.set_zlabel('Amplitude / Resonanzsignal')

# Titel hinzufügen
ax.set_title('3D-Visualisierung der Resonanz und Entropie')

# Plot anzeigen
plt.show()

logging.info("Programm erfolgreich abgeschlossen.")
