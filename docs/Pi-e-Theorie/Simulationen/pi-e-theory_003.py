import numpy as np
import matplotlib.pyplot as plt

# Zeitachse
t = np.linspace(0, 10, 1000)

# Grundfrequenzen
f_pi = np.pi
f_e = np.e

# Einzelne Schwingungen
signal_pi = np.sin(2 * np.pi * f_pi * t)          # π = natürliche Grundresonanz
signal_e = np.sin(2 * np.pi * f_e * t)            # e = evolutionäre Veränderung / Lernimpuls

# Bewusstseinsfaktor (zwischen 0 und 1)
alpha = 0.5  # 0 = neutral, 1 = maximale Beeinflussung durch e

# Kombiniertes Resonanzsignal mit bewusster Modulation
signal = signal_pi + alpha * signal_e

# Energie: Amplitude²
energy = signal**2

# Strukturentropie: Gleitender Mittelwert der Energie
window = 50
entropy = np.convolve(energy, np.ones(window)/window, mode='same')

# Plot
plt.figure(figsize=(12, 8))

# 1. Resonanzsignal
plt.subplot(3, 1, 1)
plt.plot(t, signal, label='π + α·e Resonanz', color='blue')
plt.title('Bewusst moduliertes Resonanzfeld (π + α·e)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# 2. Energieverlauf
plt.subplot(3, 1, 2)
plt.plot(t, energy, label='Energie (Amplitude²)', color='red')
plt.ylabel('Energie')
plt.grid(True)
plt.legend()

# 3. Strukturentropie
plt.subplot(3, 1, 3)
plt.plot(t, entropy, label='Strukturentropie (Pseudo)', color='green')
plt.xlabel('Zeit')
plt.ylabel('Strukturentropie')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
