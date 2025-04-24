import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Konstanten
k_B = 1.38e-23  # Boltzmann-Konstante in J/K
gamma = 0.1     # Dämpfungsfaktor
omega_ext = 2 * np.pi  # Externe Anregungsfrequenz (z.B. 1 Hz)
A_values = np.linspace(0.1, 2, 100)  # Amplitudenbereich
omega_0_values = np.linspace(0.5, 3.0, 100)  # Resonanzfrequenzbereich (Hz)

# Meshgrid für 2D-Daten
A, omega_0 = np.meshgrid(A_values, omega_0_values)

# Berechnung der Resonanzenergie
E_resonance = A / (1 + ((omega_ext - omega_0) / gamma)**2)

# Berechnung der Entropie
entropy = k_B * np.log(1 + ((omega_ext - omega_0) / gamma)**2)  # Entropie

# 3D-Plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot der Resonanzenergie und Entropie
surf = ax.plot_surface(A, omega_0, E_resonance, cmap='inferno', edgecolor='none', alpha=0.6)
ax.set_xlabel('Amplitude (A)')
ax.set_ylabel('Resonanzfrequenz (Hz)')
ax.set_zlabel('Resonanzenergie (J)')
ax.set_title('Resonanzfrequenz, Energie und Entropie')

# Entropieoberfläche ebenfalls darstellen
surf_entropy = ax.plot_surface(A, omega_0, entropy, cmap='viridis', edgecolor='none', alpha=0.3)

# Farbbalken für die Resonanzenergie und Entropie
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Resonanzenergie')
fig.colorbar(surf_entropy, ax=ax, shrink=0.5, aspect=10, label='Entropie')

plt.show()
