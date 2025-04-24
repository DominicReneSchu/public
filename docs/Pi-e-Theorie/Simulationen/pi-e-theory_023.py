import numpy as np
import matplotlib.pyplot as plt
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Parameter
k_B = 1  # Boltzmann-Konstante (vereinfacht)
alpha = 1  # Konstante für die Entropieberechnung
A = 1  # Amplitude der Resonanz
omega_0 = 2 * np.pi  # Resonanzfrequenz (z.B. 1 Hz)
gamma = 0.1  # Breite der Resonanz

# Funktion für die Resonanzenergie
def E_resonance(omega):
    return A / (1 + ((omega - omega_0) / gamma) ** 2)

# Funktion für die Entropie
def entropy(omega):
    E = E_resonance(omega)
    return k_B * alpha * np.log(E)

# Frequenzbereich
omega_values = np.linspace(0, 2 * np.pi, 500)

# Entropie berechnen
entropy_values = np.array([entropy(omega) for omega in omega_values])

# Plot der Entropie in Abhängigkeit von der Frequenz
plt.plot(omega_values, entropy_values, label="Entropie S(ω)", color='b')
plt.axvline(omega_0, color='r', linestyle='--', label="Resonanzfrequenz ω₀")
plt.xlabel('Frequenz (ω)')
plt.ylabel('Entropie (S(ω))')
plt.title('Entropie in Abhängigkeit von der Frequenz')
plt.legend()
plt.grid(True)
plt.show()
