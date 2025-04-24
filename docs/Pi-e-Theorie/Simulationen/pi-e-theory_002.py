import numpy as np
import matplotlib.pyplot as plt
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Zeitachse
t = np.linspace(0, 10, 1000)

# Grundschwingungen mit π und e
f_pi = np.pi
f_e = np.e
signal_pi = np.sin(2 * np.pi * f_pi * t)
signal_e = np.sin(2 * np.pi * f_e * t)

# Überlagerung (Resonanz)
signal = signal_pi + signal_e

# Energie (Amplitude²)
energy = signal**2

# Pseudo-Entropie: Gleitender Mittelwert der Energie
window = 50
entropy = np.convolve(energy, np.ones(window)/window, mode='same')

# Plot
plt.figure(figsize=(12, 8))

# Signal
plt.subplot(3, 1, 1)
plt.plot(t, signal, label='π + e Resonanz', color='blue')
plt.title('Resonanzüberlagerung von π und e')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Energieverlauf
plt.subplot(3, 1, 2)
plt.plot(t, energy, label='Energie (Amplitude²)', color='red')
plt.ylabel('Energie')
plt.grid(True)
plt.legend()

# Entropie (symbolisch)
plt.subplot(3, 1, 3)
plt.plot(t, entropy, label='Pseudo-Entropie', color='green')
plt.xlabel('Zeit')
plt.ylabel('Entropie')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
