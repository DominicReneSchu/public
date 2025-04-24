import numpy as np
import matplotlib.pyplot as plt
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Parameter
m = 1e-26  # Masse der Atome (kg)
omega_0 = 2 * np.pi * 1e13  # Eigenfrequenz des Systems (rad/s)
A_0 = 1e-10  # Anfangsamplitude (m)
alpha = 0.5  # Amplituden-Exponent
E_0 = 1e-6  # Ausgangsenergiebarriere
omega_max = 1e15  # Maximale Resonanzfrequenz (rad/s)
beta = 0.3  # Energiebarriere-Exponent

# Dehnung (von 0 bis 0.1)
epsilon = np.linspace(0, 0.1, 500)

# Resonanzenergie
A = A_0 * (1 + epsilon) ** alpha
omega = omega_0 * (1 + epsilon)  # Frequenzänderung mit Dehnung
E_resonance = 0.5 * m * omega**2 * A**2  # Phonon-Energie

# Energiebarriere
E_barrier = E_0 * (1 + (omega**2 / omega_max**2)) * (1 + epsilon) ** beta

# Gesamte Energie
E_total = E_resonance + E_barrier

# Verstärkung der Signale um eine Potenz von 10 (für alle Energien)
E_resonance *= 1e8  # Resonanzenergie verstärken
E_barrier *= 1e4  # Energiebarriere verstärken
E_total *= 1e4  # Gesamtenergie verstärken

# Plot der Resonanzenergie, Energiebarriere und Gesamtenergie mit logarithmischer Skalierung
plt.figure(figsize=(10, 6))
plt.plot(epsilon, E_resonance, label="Resonanzenergie", color='blue')
plt.plot(epsilon, E_barrier, label="Energiebarriere", color='red')
plt.plot(epsilon, E_total, label="Gesamtenergie", color='green', linestyle='--')

# Logarithmische Skalierung der Y-Achse
plt.yscale('log')

plt.title('Energie im Lüdersdehnungsbereich (logarithmisch, verstärkt)')
plt.xlabel('Dehnung (ε)')
plt.ylabel('Energie (J) (log-Skala)')
plt.legend()
plt.grid(True, which='both', ls='--')
plt.show()
