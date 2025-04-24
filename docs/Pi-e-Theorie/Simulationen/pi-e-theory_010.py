import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Beispiel für die Berechnungen
def berechnungen(T, A):
    # Verhindern von unendlich hohen Werten (Singularität) bei Logarithmus und Division
    epsilon = 1e-10  # Kleine Zahl zur Stabilisierung der Berechnungen
    energie = np.log(np.maximum(T**2 + A**2, epsilon))  # Sicherstellen, dass der Wert immer größer als 0 ist
    entropy = np.log(np.maximum(T + A, epsilon))  # Verhindert Logarithmus von 0
    return energie, entropy

# Generiere Werte für T und A (x, y Achsen)
T = np.linspace(-10, 10, 100)
A = np.linspace(-10, 10, 100)
T, A = np.meshgrid(T, A)

# Berechnungen für Energie und Entropie
energie, entropy = berechnungen(T, A)

# Visualisierung: 3D-Oberfläche für Energie
fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(T, A, energie, cmap='inferno', edgecolor='none')
ax.set_title('Energie')

# Visualisierung: 3D-Oberfläche für Entropie
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(T, A, entropy, cmap='inferno', edgecolor='none')
ax2.set_title('Entropie')

plt.show()
