import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Konstanten
pi = np.pi
h = 6.626e-34

# Raumgitter (x, y, z von -1 bis 1)
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
z = np.linspace(-1, 1, 100)
X, Y, Z = np.meshgrid(x, y, z)

# Zeit (Beispielzeitpunkt)
t = 0.01

# Frequenzfeld f(x, y, z, t): stehende Kugelwelle
f = np.sin(10 * pi * X) * np.sin(10 * pi * Y) * np.sin(10 * pi * Z) * np.cos(2 * pi * 5 * t)

# Kopplungsdichte σ(x, y, z): 3D-Gaußverteilung zentriert bei (0,0,0)
sigma = np.exp(-20 * (X**2 + Y**2 + Z**2))

# Schu-Gleichung in 3D
E = sigma * pi * h * f

# 3D-Schnitt (z=0-Ebene)
mid = E.shape[2] // 2
E_slice = E[:, :, mid]

# Visualisierung (2D-Schnitt aus 3D-Feld)
plt.figure(figsize=(6, 5))
plt.contourf(x, y, E_slice, levels=100, cmap='plasma')
plt.colorbar(label='Energieverteilung E(x, y, z=0)')
plt.title('3D-Kraftfeldknoten (Schnitt z=0) mit Zeit-Oszillation')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.tight_layout()
plt.show()
