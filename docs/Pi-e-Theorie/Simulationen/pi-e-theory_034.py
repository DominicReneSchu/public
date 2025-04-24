import numpy as np
import matplotlib.pyplot as plt
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Parameter
omega_0 = 2 * np.pi  # Resonanzfrequenz (Hz)
gamma = 0.1  # Dämpfungsfaktor
A = np.linspace(0.1, 1, 500)  # Amplitude (verändert)
T = np.linspace(0, 10, 500)  # Zeit/Frequenz (verändert)

# Reshaping der T- und A-Arrays für Meshgrid
T_grid, A_grid = np.meshgrid(T, A)

# Berechnung der Resonanzenergie
omega_ext = omega_0 + A_grid  # Äußere Frequenz (simuliert durch Amplitude)
E_resonance = A_grid / (1 + ((omega_ext - omega_0) / gamma)**2)  # Resonanzenergie

# Entropieberechnung (logarithmisch)
entropy = -E_resonance * np.log(E_resonance)  # Entropie (vereinfacht)

# Entropie korrekt umformen, um sie als 2D-Daten für die Visualisierung zu verwenden
entropy_grid = np.reshape(entropy, (len(A), len(T)))

# Logarithmische Skalierung der Entropie
entropy_grid_log = np.log10(entropy_grid + 1e-6)  # Kleine Verschiebung, um log(0) zu vermeiden

# Visualisierung
fig = plt.figure(figsize=(16, 10))

# Plot der Resonanzenergie
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(T_grid, A_grid, E_resonance, cmap='inferno', edgecolor='none')
ax1.set_xlabel('Zeit / Frequenz')
ax1.set_ylabel('Amplitude')
ax1.set_zlabel('Resonanzenergie')
ax1.set_title('Resonanzenergie')

# Plot der Entropie mit log-Skalierung
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(T_grid, A_grid, entropy_grid_log, cmap='plasma', edgecolor='none')
ax2.set_xlabel('Zeit / Frequenz')
ax2.set_ylabel('Amplitude')
ax2.set_zlabel('Log(Entropie)')
ax2.set_title('Log-Entropie')

# Verbessern der Darstellung
plt.tight_layout()
plt.show()
