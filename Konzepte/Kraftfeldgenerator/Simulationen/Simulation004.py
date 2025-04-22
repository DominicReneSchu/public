import numpy as np
import matplotlib.pyplot as plt

# Konstanten
pi = np.pi                         # Kreiszahl Pi (Schu-Kompass)
h = 6.626e-34                      # Plancksches Wirkungsquantum in J·s
f_ion = 1e9                         # Resonanzfrequenz der Ionen in Hz (angepasst für Ionisation)
sigma_ion = 1e6                     # Resonanzkopplungsdichte der Ionen

# Raumgitter definieren (x, y im Bereich -1 bis 1)
x = np.linspace(-1, 1, 400)
y = np.linspace(-1, 1, 400)
X, Y = np.meshgrid(x, y)

# Ionisationsfeld f(x, y): sinusförmige Wellen (moduliert durch Frequenz)
f = np.sin(2 * pi * f_ion * X) * np.sin(2 * pi * f_ion * Y)

# Kopplungsdichte σ(x, y): Gaußförmige Feldverstärkung zentriert bei (0,0)
sigma = np.exp(-20 * (X**2 + Y**2))

# Schu-Gleichung: E(x, y) = σ · π · h · f (für ionisierte Teilchen)
E = sigma * pi * h * f

# Visualisierung der Energieverteilung
plt.figure(figsize=(6, 5))
plt.contourf(X, Y, E, levels=100, cmap='viridis')
plt.colorbar(label='Energieverteilung E(x, y)')
plt.title('Ionenfalle Simulation mit Schu-Gleichung')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(False)
plt.tight_layout()
plt.show()
