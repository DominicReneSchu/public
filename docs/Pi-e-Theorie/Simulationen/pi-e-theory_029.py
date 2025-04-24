import numpy as np
import matplotlib.pyplot as plt
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Konstanten
k_B = 1.380649e-23  # Boltzmann-Konstante (J/K)
omega_0 = 2 * np.pi * 1e3  # Resonanzfrequenz (rad/s)
gamma = 50  # Dämpfungskonstante
T = 300  # Temperatur in Kelvin
A = 1  # Normierte Amplitude

# Frequenzspektrum
omega = np.linspace(omega_0 - 500, omega_0 + 500, 1000)

# Entropie-Berechnung (normiert)
entropy = k_B * np.log(1 / (1 + ((omega - omega_0) / gamma)**2))
entropy_norm = entropy / np.max(np.abs(entropy))  # Normiert für Vergleich

# Resonanzenergie (Lorentz-Kurve)
E_resonance = A / (1 + ((omega - omega_0) / gamma)**2)
E_resonance_norm = E_resonance / np.max(E_resonance)  # Normiert

# Plot
plt.figure(figsize=(10, 6))
plt.plot(omega, entropy_norm, label="Normierte Entropie", color='orange', linewidth=2)
plt.plot(omega, E_resonance_norm, label="Normierte Resonanzenergie", color='blue', linestyle='--', linewidth=2)

# Markierung der Resonanzfrequenz
plt.axvline(omega_0, color='gray', linestyle=':', label="Resonanzfrequenz")

plt.title("Vergleich: Entropie vs. Resonanzenergie", fontsize=14)
plt.xlabel("Frequenz (rad/s)")
plt.ylabel("Normierte Werte")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
