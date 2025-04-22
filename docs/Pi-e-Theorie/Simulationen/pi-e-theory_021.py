import numpy as np
import matplotlib.pyplot as plt

# Parameter
omega_0 = 2 * np.pi  # Eigenfrequenz des Systems (z.B. 1 Hz)
A = 1                # Amplitude
omega_ext = np.linspace(0, 2 * np.pi * 5, 500)  # Externe Frequenzen (0 bis 5 Hz)
gamma_values = [0.1, 0.5, 1.0, 2.0]  # Verschiedene Dämpfungswerte

# Resonanzenergie für unterschiedliche Dämpfungswerte berechnen
plt.figure(figsize=(8, 6))

for gamma in gamma_values:
    E_resonance = A / (1 + ((omega_ext - omega_0) / gamma)**2)
    plt.plot(omega_ext / (2 * np.pi), E_resonance, label=f'γ = {gamma}')  # Frequenz in Hz

plt.title('Resonanzkurve für verschiedene Dämpfungswerte')
plt.xlabel('Externe Frequenz (Hz)')
plt.ylabel('Resonanzenergie')
plt.legend()
plt.grid(True)
plt.show()
