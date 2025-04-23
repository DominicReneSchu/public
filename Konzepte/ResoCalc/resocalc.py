import numpy as np
import matplotlib.pyplot as plt

# Parameter
m = 2        # kg
l = 1        # m
f_r = 5      # Resonanzfrequenz in Hz
kopplung = 0.2
theta_max = 0.1

# Frequenzbereich
frequenzen = np.linspace(1, 20, 300)
omega = 2 * np.pi * frequenzen

# Trägheitsmomente
J_konv = m * l**2
J_reso = 0.5 * m * l**2

# Konventionelles Drehmoment
M_konv = J_konv * omega**2 * theta_max / np.sqrt(2)

# ResoCalc-Drehmoment
r = frequenzen / f_r
delta = np.abs(1 - r**2)
delta[delta < 0.0001] = 0.0001  # vermeiden von Division durch Null
V = 1 / delta
M_reso = J_reso * omega**2 * V * kopplung

# Plot
plt.figure(figsize=(10, 6))
plt.plot(frequenzen, M_konv, label='Konventionell', color='blue')
plt.plot(frequenzen, M_reso, label='ResoCalc', color='red')
plt.axvline(f_r, color='gray', linestyle='--', label='f_r (Resonanz)')
plt.xlabel('Frequenz (Hz)')
plt.ylabel('Effektives Drehmoment (Nm)')
plt.title('Vergleich: Konventionelle Berechnung vs. ResoCalc')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
