import numpy as np
import matplotlib.pyplot as plt
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Konstanten
k_B = 1.380649e-23  # Boltzmann-Konstante in J/K
omega_0 = 2 * np.pi * 1e3  # Resonanzfrequenz in rad/s
gamma = 50  # Dämpfungskonstante
T = 300  # Temperatur in Kelvin

# Frequenzbereich
omega = np.linspace(omega_0 - 100, omega_0 + 100, 500)

# Entropie Berechnung
entropy = k_B * np.log(1 / (1 + ((omega - omega_0) / gamma)**2))

# Plot
plt.figure(figsize=(8, 6))
plt.plot(omega, entropy, label="Entropie")
plt.xlabel("Frequenz (rad/s)")
plt.ylabel("Entropie (J/K)")
plt.title("Entropie vs. Frequenz")
plt.legend()
plt.grid(True)
plt.show()
