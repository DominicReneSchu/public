import numpy as np
import matplotlib.pyplot as plt
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Frequenzbereich
frequencies = np.linspace(0.1, 10, 1000)

# Resonanzbedingung (maximale Energie bei f = π + e)
f_resonance = np.pi + np.e

# Resonanzenergie als Gauss-Kurve um die Resonanzfrequenz
E_res = np.exp(-((frequencies - f_resonance)**2) / 0.1)

# Entropie als Gegenverlauf zur Resonanzenergie
A = 1 - E_res

plt.figure(figsize=(10, 5))
plt.plot(frequencies, E_res, label='$$E_{{Resonanz}}(f)$$', color='blue')
plt.plot(frequencies, A, label='$A(f)$ (Entropie)', color='red', linestyle='--')
plt.axvline(f_resonance, color='gray', linestyle=':', label='Resonanzfrequenz')
plt.title('Frequenzabhängigkeit von Entropie und Resonanzenergie')
plt.xlabel('Frequenz $f$')
plt.ylabel('Energie / Entropie')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
