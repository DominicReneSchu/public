import numpy as np
import matplotlib.pyplot as plt

# Physikalische Konstanten
delta = 1.5e-3     # Energielücke Niob (eV)
k_B = 8.617e-5     # Boltzmann-Konstante (eV/K)
R_res = 1e-9       # Residualwiderstand (Ω)

# Resonatorparameter
f0 = 10e9          # Resonanzfrequenz [Hz]
Q = 1e4            # Gütefaktor
T = 4              # Temperatur [K]

# Frequenzbereich
frequencies = np.linspace(1e9, 100e9, 1000)  # 1 GHz bis 100 GHz

# Verlustfaktor (BCS + Residual)
def loss_factor(f, T):
    # Berechnung des BCS-Verlustfaktors
    R_BCS = (f**2 / T) * np.exp(-delta / (k_B * T))
    # Gesamtverlustfaktor
    return (R_BCS + R_res) * np.sqrt(f / f0) / Q

# Eingangsleistung (Beispiel: 1 kW)
P_res = 1e3  # 1000 W

# Nettoleistung
P_net = P_res / (1 + loss_factor(frequencies, T))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(frequencies / 1e9, P_net, label='Nettoleistung')  # Frequenz in GHz
plt.xlabel('Frequenz [GHz]')
plt.ylabel('Nettoleistung [W]')
plt.title('Nettoleistung eines supraleitenden Resonators (Niob, 4 K)')
plt.grid(True)
plt.legend()
plt.show()
