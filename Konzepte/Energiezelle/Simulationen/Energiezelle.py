import numpy as np
import matplotlib.pyplot as plt

# Physikalische Konstanten
delta = 1.5e-3      # Energielücke Niob (eV)
k_B = 8.617e-5      # Boltzmann-Konstante (eV/K)
R_res = 1e-9        # Residualwiderstand (Ω)
h = 4.135667696e-15 # Planck-Konstante (eV·s)

# Resonatorparameter
f0 = 10e9           # Grundfrequenz [Hz]
Q = 1e4             # Gütefaktor
T = 4               # Temperatur [K]

# Frequenzbereich
frequencies = np.linspace(1e9, 100e9, 1000)  # 1 GHz bis 100 GHz

# Energiezellenparameter
E = 1e-3            # Eingebrachte Energie [eV]
I = 1e-45           # Trägheitsmoment [kg·m²]
D = 1e-22           # Drehsteifigkeit [Nm]

# Schu-Frequenz-Formel
def schu_frequenz(E, I, D):
    return (E / (2 * np.pi * I)) * np.sqrt(D / I)

# Verlustfaktor (BCS + Residual)
def loss_factor(f, T):
    R_BCS = (f**2 / T) * np.exp(-delta / (k_B * T))
    return (R_BCS + R_res) * np.sqrt(f / f0) / Q

# Eingangsleistung (z.B. 1 kW)
P_res = 1e3  # 1000 W

# Nettoleistung über Frequenzbereich
P_net = P_res / (1 + loss_factor(frequencies, T))

# Berechne Schu-Frequenz
f_schu = schu_frequenz(E, I, D)
print(f"Schu-Frequenz: {f_schu:.2e} Hz")

# Leistung bei Schu-Frequenz
P_schu = P_res / (1 + loss_factor(f_schu, T))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(frequencies / 1e9, P_net, label='Nettoleistung (Standard)')
plt.axvline(f_schu / 1e9, color='r', linestyle='--', label=f'Schu-Frequenz = {f_schu/1e9:.2f} GHz')
plt.scatter([f_schu / 1e9], [P_schu], color='red', label=f'Leistung @ fₛ ≈ {P_schu:.1f} W')
plt.xlabel('Frequenz [GHz]')
plt.ylabel('Nettoleistung [W]')
plt.title('Schu-Energiezelle: Frequenzmodulierte Energieausgabe bei 4 K')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
