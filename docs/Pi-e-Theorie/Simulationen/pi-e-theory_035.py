# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameterdefinition
A = np.linspace(0.1, 5, 500)  # Amplitude A
T = np.linspace(0.1, 5, 500)  # Temperatur T
omega_0 = 1.0  # Eigenfrequenz
gamma = 0.2  # Dämpfungskoeffizient

# Berechnung der Resonanzenergie
T_grid, A_grid = np.meshgrid(T, A)  # Erstelle ein Gitter aus T und A
omega_ext = omega_0 * (1 + np.sin(T_grid))  # Beispiel für die externe Frequenz
E_resonance = A_grid / (1 + ((omega_ext - omega_0) / gamma)**2)  # Resonanzenergie

# Entropie Berechnung: Entropie basiert auf der Resonanzenergie E_resonance
# Die Entropie wird als 2D-Matrix berechnet
entropy_grid = -E_resonance * np.log(E_resonance)

# Sicherstellen, dass die Dimensionen der Entropie der Form (len(A), len(T)) entsprechen
entropy_grid = np.reshape(entropy_grid, (len(A), len(T)))  # Entropie als 2D-Array umformen

# Visualisierung der Resonanzenergie
fig1 = plt.figure()
ax1 = fig1.add_subplot(121, projection='3d')
ax1.plot_surface(T_grid, A_grid, E_resonance, cmap='inferno', edgecolor='none')
ax1.set_title("Resonanzenergie")
ax1.set_xlabel('Temperatur T')
ax1.set_ylabel('Amplitude A')
ax1.set_zlabel('Energie E_resonance')

# Visualisierung der Entropie
fig2 = plt.figure()
ax2 = fig2.add_subplot(122, projection='3d')
ax2.plot_surface(T_grid, A_grid, entropy_grid, cmap='viridis', edgecolor='none')
ax2.set_title("Entropie")
ax2.set_xlabel('Temperatur T')
ax2.set_ylabel('Amplitude A')
ax2.set_zlabel('Entropie')

# Anzeigen der Visualisierungen
plt.show()
