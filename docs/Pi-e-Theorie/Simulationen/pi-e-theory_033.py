import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter für die Resonanz
omega_0 = 2 * np.pi  # Eigenfrequenz des Systems
gamma = 0.1  # Dämpfungskoeffizient
A = np.logspace(-3, 2, 500)  # Amplituden in logarithmischer Skala
T = np.linspace(0, 10, 500)  # Zeit oder Parameter für Frequenz

# Resonanzfrequenzen und Entropie berechnen
omega_ext = omega_0 + 0.1 * np.sin(T)  # Frequenzen schwanken leicht um die Resonanzfrequenz

# Erstellen des Gitters
A_grid, T_grid = np.meshgrid(A, T)  # 2D-Gitter für die Visualisierung

# Resonanzenergie auf dem Gitter
E_resonance_grid = A_grid / (1 + ((omega_ext - omega_0) / gamma)**2)

# Entropie berechnen auf dem Gitter
# Entropie ist eine Summe über E_resonance * log(E_resonance) für jedes (A, T)-Paar
entropy_grid = -E_resonance_grid * np.log(E_resonance_grid)

# Visualisierung der Resonanzenergie und Entropie
fig = plt.figure(figsize=(16, 10))

# Plot der Resonanzenergie
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(T_grid, A_grid, E_resonance_grid, cmap='inferno', edgecolor='none')
ax1.set_xlabel('Zeit / Frequenz')
ax1.set_ylabel('Amplitude')
ax1.set_zlabel('Resonanzenergie')
ax1.set_title('Resonanzenergie')

# Plot der Entropie
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(T_grid, A_grid, entropy_grid, cmap='viridis', edgecolor='none')
ax2.set_xlabel('Zeit / Frequenz')
ax2.set_ylabel('Amplitude')
ax2.set_zlabel('Entropie')
ax2.set_title('Entropie')

# Verbessern der Darstellung
plt.tight_layout()
plt.show()
