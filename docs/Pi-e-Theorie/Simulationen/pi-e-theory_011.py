import numpy as np
import matplotlib.pyplot as plt
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Parameter
k_B = 1.38e-23  # Boltzmann-Konstante in J/K
A = 1.0  # Amplitude
omega = 2 * np.pi  # Frequenz
time = np.linspace(0, 10, 1000)  # Zeit

# Energie als Funktion der Zeit
energy = A * np.sin(omega * time)**2

# Entropie als Funktion der Energie
entropy = k_B * np.log(energy)

# Plot der Energie und Entropie
plt.figure(figsize=(10, 5))

# Energie plotten
plt.subplot(1, 2, 1)
plt.plot(time, energy, label='Energie', color='blue')
plt.title('Energie über Zeit')
plt.xlabel('Zeit (s)')
plt.ylabel('Energie (J)')
plt.grid()

# Entropie plotten
plt.subplot(1, 2, 2)
plt.plot(time, entropy, label='Entropie', color='red')
plt.title('Entropie über Zeit')
plt.xlabel('Zeit (s)')
plt.ylabel('Entropie (J/K)')
plt.grid()

plt.tight_layout()
plt.show()
