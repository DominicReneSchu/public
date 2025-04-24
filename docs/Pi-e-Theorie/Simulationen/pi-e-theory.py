# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Parameterraum
f = np.linspace(0.1, 4 * np.pi, 200)  # Frequenz
A = np.linspace(0.1, 2, 200)          # Amplitude
F, A_grid = np.meshgrid(f, A)

# Resonanzenergie: Maximum bei 2p
E_res = A_grid**2 * np.exp(-((F - 2*np.pi)**2))

# Entropie: nimmt bei Resonanz ab
S = (1 / A_grid) * np.exp((F - 2*np.pi)**2)

# Visualisierung
fig = plt.figure(figsize=(14, 6))

# Plot Resonanzenergie
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(F, A_grid, E_res, cmap='plasma')
ax1.set_title("Resonanzenergie")
ax1.set_xlabel("Frequenz (f)")
ax1.set_ylabel("Amplitude (A)")
ax1.set_zlabel("E_res")

# Plot Entropie
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(F, A_grid, S, cmap='viridis')
ax2.set_title("Entropie")
ax2.set_xlabel("Frequenz (f)")
ax2.set_ylabel("Amplitude (A)")
ax2.set_zlabel("Entropie S")

plt.tight_layout()
plt.show()
