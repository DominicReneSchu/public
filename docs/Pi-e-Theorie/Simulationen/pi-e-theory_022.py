import numpy as np
import matplotlib.pyplot as plt
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Parameter
omega_0 = 2 * np.pi  # Eigenfrequenz des Systems
gamma = 0.1  # Dämpfung
A = 1  # Amplitude
k_B = 1.38e-23  # Boltzmann-Konstante
omega_ext = np.linspace(omega_0 - 10, omega_0 + 10, 500)  # Externe Frequenzen

# Resonanzenergie
E_resonance = A / (1 + ((omega_ext - omega_0) / gamma) ** 2)

# Entropie berechnen: Einfache Entropieberechnung (logarithmisch)
Omega = np.exp(E_resonance)  # Anzahl der Zustände als Funktion der Energie
S = k_B * np.log(Omega)

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot der Resonanzenergie
ax1.plot(omega_ext, E_resonance, label="Resonanzenergie", color='b')
ax1.set_xlabel('Externe Frequenz (ω_ext)')
ax1.set_ylabel('Energie (E_resonance)')
ax1.set_title('Resonanzkurve')
ax1.legend()

# Plot der Entropie
ax2.plot(omega_ext, S, label="Entropie", color='r')
ax2.set_xlabel('Externe Frequenz (ω_ext)')
ax2.set_ylabel('Entropie (S)')
ax2.set_title('Entropie-Entwicklung')
ax2.legend()

plt.tight_layout()
plt.show()
