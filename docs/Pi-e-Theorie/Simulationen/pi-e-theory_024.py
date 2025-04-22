import numpy as np
import matplotlib.pyplot as plt

# Konstanten und Parameter
k_B = 1.38e-23  # Boltzmann-Konstante in J/K
A = 1.0  # Amplitude (Beliebiger Wert)
omega_0 = 2 * np.pi  # Eigenfrequenz des Systems (z.B. 1 Hz)
gamma = 0.1  # Dämpfungskonstante
T = 300  # Temperatur in Kelvin

# Frequenzbereich
omega_min = 0.1 * omega_0  # Frequenzbereich von 0.1 * omega_0 bis 2 * omega_0
omega_max = 2 * omega_0
omega = np.linspace(omega_min, omega_max, 500)

# Berechnung der Resonanzenergie E_res(omega)
E_resonance = A / (1 + ((omega - omega_0) / gamma)**2)

# Berechnung der Entropie S(omega, T) = E_res(omega) / T
S = E_resonance / T

# Berechnung der Gesamtenergie (falls gewünscht)
E_total = E_resonance  # In diesem Fall ist die Gesamtenergie einfach die Resonanzenergie

# Integrieren der Entropie über den Frequenzbereich
S_total = np.trapz(S, omega)

# Plot der Resonanzenergie und Entropie als Funktion der Frequenz
plt.figure(figsize=(10, 6))
plt.plot(omega, E_resonance, label='Resonanzenergie E_res(ω)', color='b')
plt.plot(omega, S, label='Entropie S(ω, T)', color='r')
plt.xlabel('Frequenz (ω)')
plt.ylabel('Energie / Entropie')
plt.title('Resonanzenergie und Entropie als Funktion der Frequenz')
plt.grid(True)
plt.legend()
plt.show()

# Gesamtentropie
print(f"Gesamtentropie im Frequenzbereich: {S_total:.4e} J/K")
