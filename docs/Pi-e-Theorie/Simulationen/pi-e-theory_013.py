import numpy as np
import matplotlib.pyplot as plt
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Systemparameter
omega_0 = 2 * np.pi  # Eigenfrequenz des Systems (z.B. 1 Hz)
gamma = 0.1          # Dämpfungsfaktor
A = 1                # Amplitude
omega_ext = np.linspace(omega_0 - 2, omega_0 + 2, 400)  # Frequenzbereich um die Eigenfrequenz

# Berechnungen
E_resonance = A / (1 + ((omega_ext - omega_0) / gamma)**2)  # Resonanzenergie
entropy = np.log(E_resonance + 1e-5)  # Entropie (logarithmisch)

# Plot für die Resonanzenergie
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(omega_ext, E_resonance, label="Resonanzenergie", color='blue')
plt.title("Resonanzenergie vs Frequenz")
plt.xlabel("Frequenz (Hz)")
plt.ylabel("Resonanzenergie")
plt.grid(True)
plt.legend()

# Plot für die Entropie
plt.subplot(2, 1, 2)
plt.plot(omega_ext, entropy, label="Entropie", color='red')
plt.title("Entropie vs Frequenz")
plt.xlabel("Frequenz (Hz)")
plt.ylabel("Entropie (logarithmisch)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

