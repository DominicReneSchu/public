import numpy as np
import matplotlib.pyplot as plt
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

# Visualisierung der Ergebnisse
plt.figure(figsize=(10, 6))

# Plot der Resonanzenergie
plt.contourf(A, omega_ext, E_resonance, cmap='inferno', levels=50)
plt.colorbar(label="Resonanzenergie")
plt.title('Resonanzenergie im System mit Dämpfung')
plt.xlabel('Amplitude (A)')
plt.ylabel('Äußere Frequenz (ω_ext)')
plt.show()

# Plot der Phonon-Energie
plt.contourf(A, omega_ext, phonon_energy, cmap='plasma', levels=50)
plt.colorbar(label="Phonon-Energie")
plt.title('Phonon-Energie im System mit Dämpfung')
plt.xlabel('Amplitude (A)')
plt.ylabel('Äußere Frequenz (ω_ext)')
plt.show()

# Plot der Gesamtenergie
plt.contourf(A, omega_ext, total_energy, cmap='viridis', levels=50)
plt.colorbar(label="Gesamtenergie")
plt.title('Gesamtenergie im System mit Dämpfung')
plt.xlabel('Amplitude (A)')
plt.ylabel('Äußere Frequenz (ω_ext)')
plt.show()
