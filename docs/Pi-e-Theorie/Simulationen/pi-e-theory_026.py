import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Konstanten
k_B = 1.380649e-23  # Boltzmann-Konstante in J/K
omega_0 = 2 * np.pi  # Eigenfrequenz des Systems
gamma = 0.1  # Dämpfungsfaktor
A = 1e-4  # Amplitude
omega_ext = np.linspace(0.5, 1.5, 500)  # Äußere Frequenz

# Resonanzenergie
E_resonance = A / (1 + ((omega_ext - omega_0) / gamma) ** 2)

# Temperaturabhängigkeit der Entropie
T = np.linspace(0.1, 100, 500)  # Temperaturbereich

# Entropie als Funktion der Temperatur
S = k_B * np.log(E_resonance[:, np.newaxis] / (k_B * T))

# Erstellen der 3D-Darstellung
T_mesh, omega_ext_mesh = np.meshgrid(T, omega_ext)
S_mesh = k_B * np.log(E_resonance[:, np.newaxis] / (k_B * T_mesh))

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot der Oberfläche (Entropie) im 3D-Raum
ax.plot_surface(T_mesh, omega_ext_mesh, S_mesh, cmap='inferno', edgecolor='none')

# Achsenbeschriftungen
ax.set_xlabel('Temperatur (K)')
ax.set_ylabel('Resonanzfrequenz (Hz)')
ax.set_zlabel('Entropie (J/K)')

ax.set_title('3D Darstellung der Entropie als Funktion von Temperatur und Resonanzfrequenz')

# Anzeige der Grafik
plt.show()
