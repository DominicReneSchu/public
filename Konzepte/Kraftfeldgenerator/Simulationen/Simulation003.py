import numpy as np
import matplotlib.pyplot as plt

# Konstanten
pi = np.pi
h = 6.626e-34

# Raumgitter
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
z = np.linspace(-1, 1, 100)
X, Y, Z = np.meshgrid(x, y, z)

# Zeit
t = 0.02

# Frequenzfeld f(x, y, z, t): stehende Welle in x- und y-Richtung (z = statisch)
f = np.sin(10 * pi * X) * np.sin(10 * pi * Y) * np.cos(2 * pi * 3 * t)

# Kopplung σ(x, y, z): Flächige Kopplungszone um z = 0 (Resonanzwand)
sigma = np.exp(-50 * (Z**2))  # Nur entlang z eng begrenzt

# Schu-Gleichung (Resonanzwand)
E = sigma * pi * h * f

# 2D-Schnitt bei z = 0 (die Wand-Energieverteilung)
mid = E.shape[2] // 2
E_slice = E[:, :, mid]

# Visualisierung
plt.figure(figsize=(6, 5))
plt.contourf(x, y, E_slice, levels=100, cmap='inferno')
plt.colorbar(label='Energie E(x, y, z=0)')
plt.title('Resonanz-Wand bei z = 0 (Kraftfeld-Ebene)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.tight_layout()
plt.show()
