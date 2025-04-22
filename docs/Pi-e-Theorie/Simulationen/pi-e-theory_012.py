import numpy as np
import matplotlib.pyplot as plt

# Parameter definieren
omega_0 = 2 * np.pi  # Eigenfrequenz des Systems
gamma = 0.1  # Dämpfungskoeffizient
A = 1.0  # Amplitude des Systems

# Definiere eine Array von externen Frequenzen (omega_ext)
omega_ext = np.linspace(0.5 * omega_0, 1.5 * omega_0, 400)  # Array von Frequenzen von 0.5*omega_0 bis 1.5*omega_0

# Berechnung der Resonanzenergie
E_resonance = A / (1 + ((omega_ext - omega_0) / gamma)**2)

# Berechnung der Entropie
entropy = np.log(E_resonance + 1e-10)  # Entropie als log(E_resonance), mit kleiner Zahl zur Vermeidung von log(0)

# Visualisierung der Resonanzenergie
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(omega_ext, E_resonance, label='Resonanzenergie')
plt.title('Resonanzenergie als Funktion der externen Frequenz')
plt.xlabel('Externe Frequenz (ω_ext)')
plt.ylabel('Resonanzenergie (E)')
plt.grid(True)
plt.legend()

# Visualisierung der Entropie
plt.subplot(1, 2, 2)
plt.plot(omega_ext, entropy, label='Entropie', color='r')
plt.title('Entropie als Funktion der externen Frequenz')
plt.xlabel('Externe Frequenz (ω_ext)')
plt.ylabel('Entropie')
plt.grid(True)
plt.legend()

# Plot anzeigen
plt.tight_layout()
plt.show()
