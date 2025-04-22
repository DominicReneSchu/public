import numpy as np
import matplotlib.pyplot as plt

# Parameter des Systems
m = 1.0  # Masse in kg
k = 1.0  # Federkonstante in N/m
gamma = 0.1  # Dämpfungskoeffizient in kg/s
A = 1.0  # Amplitude der Schwingung

# Resonanzfrequenz des Systems
omega_0 = np.sqrt(k / m)

# Erstellen eines Bereichs für die externe Frequenz omega_ext
omega_ext = np.linspace(0.1, 2.0 * omega_0, 500)

# Berechnung der Resonanzenergie
E_resonance = A / (1 + ((omega_ext - omega_0) / gamma)**2)

# Plotten der Resonanzkurve
plt.figure(figsize=(10, 6))
plt.plot(omega_ext, E_resonance, label=r"$E_{\text{resonance}}(\omega_{\text{ext}})$", color='blue')
plt.axvline(omega_0, color='red', linestyle='--', label=r'$\omega_0$ (Resonanzfrequenz)')
plt.title('Resonanzkurve: Energie in Abhängigkeit von der externen Frequenz')
plt.xlabel(r'Externe Frequenz $\omega_{\text{ext}}$')
plt.ylabel(r'Verhältnis der Energie $E_{\text{resonance}}$')
plt.legend()
plt.grid(True)
plt.show()
