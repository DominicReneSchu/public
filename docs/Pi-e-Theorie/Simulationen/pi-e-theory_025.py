import numpy as np
import matplotlib.pyplot as plt
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
# Da S = k_B * ln(E / (k_B * T)), und T > 0, berechnen wir S für verschiedene T-Werte.
T = np.linspace(0.1, 100, 500)  # Temperaturbereich

# Entropie als Funktion der Temperatur
S = k_B * np.log(E_resonance[:, np.newaxis] / (k_B * T))

# Plot der Entropie
plt.figure(figsize=(10, 6))
plt.contourf(T, omega_ext, S, levels=50, cmap='inferno')
plt.colorbar(label="Entropie (J/K)")
plt.xlabel('Temperatur (K)')
plt.ylabel('Resonanzfrequenz (Hz)')
plt.title('Entropie als Funktion von Temperatur und Resonanzfrequenz')
plt.show()
