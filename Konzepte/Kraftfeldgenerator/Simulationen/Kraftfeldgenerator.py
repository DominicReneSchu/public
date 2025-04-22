import numpy as np
import matplotlib.pyplot as plt

# Konstanten
pi = np.pi                         # Kreiszahl Pi (Schu-Kompass)
h = 6.626e-34                      # Plancksches Wirkungsquantum in J·s

# Raumgitter definieren (x, y im Bereich -1 bis 1)
x = np.linspace(-1, 1, 400)
y = np.linspace(-1, 1, 400)
X, Y = np.meshgrid(x, y)

# Resonanzfrequenzfeld f(x, y): stehende Wellenform
f = np.sin(10 * pi * X) * np.sin(10 * pi * Y)

# Wand-ähnliche Struktur (Kopplung sehr stark in der Mitte, schwächer am Rand)
sigma = np.exp(-10 * (X**2 + Y**2))  # zentrale starke Kopplung
sigma[(X > -0.2) & (X < 0.2) & (Y > -1.0) & (Y < 1.0)] = 10  # starke Wand im Bereich

# Schu-Gleichung: E(x, y) = σ · π · h · f
E = sigma * pi * h * f

# Visualisierung der Energieverteilung
plt.figure(figsize=(6, 5))
plt.contourf(X, Y, E, levels=100, cmap='viridis')
plt.colorbar(label='Energieverteilung E(x, y)')
plt.title('Simulation einer Wandstruktur')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(False)
plt.tight_layout()
plt.show()
