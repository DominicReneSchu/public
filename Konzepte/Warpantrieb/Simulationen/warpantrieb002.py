import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Raumgitter
size = 100
x = np.linspace(-5, 5, size)
y = np.linspace(-5, 5, size)
X, Y = np.meshgrid(x, y)

# Zeitvariable
t = 0
dt = 0.05
f = 160e9  # Frequenz ~160 GHz
λ = 3e8 / f  # Wellenlänge der Hintergrundstrahlung

# Warp-Blase: Zentrum und Radius
center = (0, 0)
radius = 1.5

def warp_field(t):
    # Grundresonanz (kosmische Hintergrundwelle)
    base_wave = np.sin(2 * np.pi * f * t)

    # Phasenmodulation vorne und hinten
    phase_front = np.pi      # destruktiv
    phase_back = 0           # konstruktiv

    # Abstand vom Zentrum (für Blasendefinition)
    R = np.sqrt((X - center[0])**2 + (Y - center[1])**2)

    # Front- und Rückseite definieren
    front_mask = X > center[0] + radius
    back_mask = X < center[0] - radius
    bubble_mask = R <= radius

    # Gesamtfeld initialisieren
    field = base_wave * np.ones_like(X)

    # Phasenmoduliert anpassen
    field[front_mask] = np.sin(2 * np.pi * f * t + phase_front)
    field[back_mask] = np.sin(2 * np.pi * f * t + phase_back)

    # Bubble-Innenraum bleibt „ruhig“
    field[bubble_mask] = 0

    return field

# Animation
fig, ax = plt.subplots()
im = ax.imshow(warp_field(0), cmap='RdBu', vmin=-1, vmax=1, animated=True)

def update(frame):
    global t
    t += dt
    im.set_array(warp_field(t))
    return [im]

ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.title("Warp-Blase im Raumresonanzfeld")
plt.show()
