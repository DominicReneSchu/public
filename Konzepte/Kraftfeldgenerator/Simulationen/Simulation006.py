import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Konstanten
pi = np.pi                         # Kreiszahl Pi (Schu-Kompass)
h = 6.626e-34                      # Plancksches Wirkungsquantum in J·s

# 3D-Gitter definieren (x, y, z im Bereich -1 bis 1)
x = np.linspace(-1, 1, 50)
y = np.linspace(-1, 1, 50)
z = np.linspace(-0.5, 0.5, 50)  # Tischhöhe etwas begrenzt
X, Y, Z = np.meshgrid(x, y, z)

# Resonanzfrequenzfeld f(x, y, z): stehende Wellenform in 3D
f = np.sin(10 * pi * X) * np.sin(10 * pi * Y) * np.cos(5 * pi * Z)

# Kopplungsdichte σ(x, y, z): Gaußförmige Feldverstärkung
sigma = np.exp(-20 * (X**2 + Y**2 + Z**2))

# Schu-Gleichung: E(x, y, z) = σ · π · h · f
E = sigma * pi * h * f

# Visualisierung der Energieverteilung in 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Wir visualisieren nur einen Ausschnitt des Tisches (Energieverteilung in der Z-Höhe)
ax.plot_surface(X[:,:,25], Y[:,:,25], E[:,:,25], cmap='viridis', edgecolor='none')

# Titel und Achsenbeschriftungen
ax.set_title('3D-Tischstruktur basierend auf Resonanzfeldern')
ax.set_xlabel('X-Achse')
ax.set_ylabel('Y-Achse')
ax.set_zlabel('Energieverteilung')

plt.tight_layout()
plt.show()
