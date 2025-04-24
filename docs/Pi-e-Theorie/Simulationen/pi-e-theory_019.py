import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Parameter
A = np.linspace(0.1, 10, 500)  # Amplitude
omega_ext = np.linspace(1, 10, 100)  # Äußere Frequenz
gamma = 0.1  # Dämpfungskoeffizient
omega_0 = 2 * np.pi  # Eigenfrequenz des Systems

# Meshgrid für A und omega_ext
A_grid, omega_grid = np.meshgrid(A, omega_ext)

# Berechnung der Resonanzenergie mit Dämpfung
E_resonance = A_grid / (1 + ((omega_grid - omega_0) / gamma)**2)

# Berechnung der Phonon-Energie
m = 1  # Masse
omega = omega_0  # Eigenfrequenz
phonon_energy = 0.5 * m * omega**2 * A_grid**2  # Phonon-Energie

# Berechnung der Gesamtenergie
total_energy = E_resonance + phonon_energy

# 3D-Plot vorbereiten
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Rotieren um die Amplitude (A)
X = A_grid
Y = omega_grid
Z = total_energy

# 3D-Oberfläche plotten
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Farbe und Achsen
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel('Amplitude (A)')
ax.set_ylabel('Äußere Frequenz (ω_ext)')
ax.set_zlabel('Gesamtenergie')

# Titel
ax.set_title('Gesamtenergie im System mit Dämpfung (3D)')

# Rotationsanimation (optional)
def rotate_plot():
    for angle in range(0, 360, 1):  # Drehung von 0 bis 360 Grad
        ax.view_init(azim=angle)  # Azimutalwinkel anpassen
        plt.draw()
        plt.pause(0.01)  # Kurze Pause für Animationseffekt

rotate_plot()

# Anzeigen
plt.show()
