import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
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

# Berechnung der Rotation um die y-Achse für die Resonanzfrequenz
theta = np.linspace(0, 2 * np.pi, 500)  # Winkel für die Rotation

# Wir rotieren die Resonanzfrequenz um die y-Achse
X = S_mesh * np.cos(theta[:, np.newaxis])  # Rotation entlang der x-Achse
Z = S_mesh * np.sin(theta[:, np.newaxis])  # Rotation entlang der z-Achse
Y = omega_ext_mesh  # Resonanzfrequenz entlang der y-Achse

# Erstellen des 3D-Plots
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot der Oberfläche (Entropie) im 3D-Raum mit Rotation
ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none')

# Achsenbeschriftungen
ax.set_xlabel('Entropie X')
ax.set_ylabel('Resonanzfrequenz (Hz)')
ax.set_zlabel('Entropie Z')

ax.set_title('3D Rotation der Entropie um die Resonanzfrequenz')

# Anzeige der Grafik
plt.show()
