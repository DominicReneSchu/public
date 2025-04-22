import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter
pi = np.pi
e = np.e

# Frequenz und Masse als Parameter
mass = 1.0   # Masse des Systems
frequency = 1.0  # Frequenz der Schwingung

# Zeitparameter
t = np.linspace(0, 10, 500)

# Bewusstseinsfaktor alpha (Wert zwischen 0 und 1)
alpha = np.linspace(0, 1, 50)  # Alpha variiert von 0 bis 1

# 2D-Gitter für Alpha und Zeit
T, A = np.meshgrid(t, alpha)  # Gitter für Zeit (t) und Alpha-Werte

# Berechnungsfunktionen
def resonance(t, alpha, mass, frequency):
    energy = (mass * frequency**2) * np.sin(alpha * t)**2
    if np.any(energy <= 0):
        print("Fehler: Energie darf nicht null oder negativ sein!")
    return energy

def entropy(energy):
    # Entropie-Berechnung auf Basis der Energie, sicherstellen, dass keine Nullwerte im Logarithmus
    epsilon = 1e-10  # Vermeidung von Logarithmus von null oder negativen Werten
    return -np.log(energy + epsilon)

# Berechnungen für Energie und Entropie
energy = resonance(T, A, mass, frequency)

# Entropie für jedes Element im Gitter berechnen
entropy_values = entropy(energy)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Überprüfung der Größe von Entropie und Energie
print("Energie:", energy[:10])  # Zeigt die ersten 10 Energie-Werte an
print("Entropie:", entropy_values[:10])  # Zeigt die ersten 10 Entropie-Werte an

# Oberfläche plotten (Energie)
ax.plot_surface(T, A, energy, cmap='inferno', edgecolor='none')
ax.set_xlabel('Zeit')
ax.set_ylabel('Alpha')
ax.set_zlabel('Energie')

# Plot Entropie als Kontur
plt.figure()
plt.contourf(T, A, entropy_values, cmap='inferno')
plt.xlabel('Zeit')
plt.ylabel('Alpha')
plt.colorbar(label="Entropie")

# Anzeige des Plots
plt.show()
