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

import numpy as np
import matplotlib.pyplot as plt

# Parameter
f_pi = np.pi       # Frequenz-Komponente aus π
f_e = np.e         # Frequenz-Komponente aus e
t = np.linspace(0, 10, 1000)  # Zeitachse

# Überlagerte Schwingung (π und e)
signal = np.sin(2 * np.pi * f_pi * t) + np.sin(2 * np.pi * f_e * t)

# Plot
plt.figure(figsize=(10, 4))
plt.plot(t, signal, label='π + e Resonanz')
plt.title('Resonanzüberlagerung π & e')
plt.xlabel('Zeit')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()