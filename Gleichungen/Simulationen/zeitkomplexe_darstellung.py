import numpy as np
import matplotlib.pyplot as plt

# Parameter
alpha = np.arccos(np.e / np.pi)  # Phasenwinkel für π/e
radius = 1  # Normierte Zeit-Hypotenuse

# Zeitkomponenten
t_real = radius * np.cos(alpha)
t_imag = radius * np.sin(alpha)

# Komplexe Energie
E_komplex = t_real + 1j * t_imag

# Plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.grid(True, which='both')

# Einheitskreis
theta = np.linspace(0, 2 * np.pi, 500)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
ax.plot(x, y, 'b', label='Einheitskreis (|E| = 1)')

# Komponenten
ax.plot([0, t_real], [0, 0], 'g--', label='Realteil (klassisch)')
ax.plot([t_real, t_real], [0, t_imag], 'orange', linestyle='dotted', label='Imaginärteil')
ax.plot([0, t_real], [0, t_imag], 'purple', label='Energie als komplexer Vektor')

# Resonanzpunkt π/e
r_resonanz = np.pi / np.e
x_res = r_resonanz * np.cos(alpha)
y_res = r_resonanz * np.sin(alpha)
ax.plot(x_res, y_res, 'ro', label='π/e-Punkt (Resonanzenergie)')

# Beschriftung
ax.set_xlabel('Reale Zeitkomponente')
ax.set_ylabel('Imaginäre Zeitkomponente')
ax.set_title('Zeitkomplexe Energieprojektion')

plt.legend()
plt.tight_layout()
plt.show()
