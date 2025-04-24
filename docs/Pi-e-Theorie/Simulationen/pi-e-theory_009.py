import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Beispielwerte (dies sollte mit den echten Werten ersetzt werden)
T = np.linspace(0.1, 10, 100)  # Beispiel Temperatur
A = np.linspace(0.1, 10, 100)  # Beispiel Alpha
T, A = np.meshgrid(T, A)  # Gitter für 2D-Daten

# Berechnete Energie und Entropie (Beispielwerte für Simulation)
energie = np.log(T**2 + A**2)  # Beispielberechnung für Energie
entropy = np.log(T + A)  # Beispielberechnung für Entropie

# 3D-Oberfläche für Energie
fig = plt.figure(figsize=(14, 7))
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(T, A, energie, cmap='inferno', edgecolor='none')
ax.set_title("Energie 3D-Oberfläche")
ax.set_xlabel('Temperatur')
ax.set_ylabel('Alpha')
ax.set_zlabel('Energie')

# 3D-Oberfläche für Entropie
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(T, A, entropy, cmap='inferno', edgecolor='none')
ax2.set_title("Entropie 3D-Oberfläche")
ax2.set_xlabel('Temperatur')
ax2.set_ylabel('Alpha')
ax2.set_zlabel('Entropie')

plt.tight_layout()
plt.show()

# 2D-Konturansicht für Energie
plt.figure(figsize=(7, 7))
plt.contourf(T, A, energie, 20, cmap='inferno')
plt.colorbar(label='Energie')
plt.title('Energie - 2D Konturansicht')
plt.xlabel('Temperatur')
plt.ylabel('Alpha')
plt.show()

# 2D-Konturansicht für Entropie
plt.figure(figsize=(7, 7))
plt.contourf(T, A, entropy, 20, cmap='inferno')
plt.colorbar(label='Entropie')
plt.title('Entropie - 2D Konturansicht')
plt.xlabel('Temperatur')
plt.ylabel('Alpha')
plt.show()
