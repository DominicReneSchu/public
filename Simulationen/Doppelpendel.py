import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Parameter des Doppelpendels
g = 9.81  # Erdbeschleunigung (m/s^2)
L1 = 1.0  # Länge des ersten Pendels (m)
L2 = 1.0  # Länge des zweiten Pendels (m)
m1 = 1.0  # Masse des ersten Pendels (kg)
m2 = 1.0  # Masse des zweiten Pendels (kg)

# Differentialgleichungen des Doppelpendels
def derivatives(t, state):
    θ1, ω1, θ2, ω2 = state

    # Berechnungen für die DGLs
    delta = θ2 - θ1
    den1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta)**2
    den2 = (L2 / L1) * den1

    dθ1_dt = ω1
    dω1_dt = ((m2 * L2 * ω2**2 * np.sin(delta) * np.cos(delta)
                + m2 * g * np.sin(θ2) * np.cos(delta)
                + m2 * L2 * np.sin(delta) * ω2**2
                - (m1 + m2) * g * np.sin(θ1))
               / den1)
    
    dθ2_dt = ω2
    dω2_dt = ((- m2 * L2 * ω2**2 * np.sin(delta) * np.cos(delta)
                + (m1 + m2) * g * np.sin(θ1) * np.cos(delta)
                - (m1 + m2) * L1 * ω1**2 * np.sin(delta)
                - (m1 + m2) * g * np.sin(θ2))
               / den2)
    
    return [dθ1_dt, dω1_dt, dθ2_dt, dω2_dt]

# Anfangswerte und Zeitspanne
theta1_0 = np.pi / 2
omega1_0 = 0.0
theta2_0 = np.pi / 2
omega2_0 = 0.0
t_span = (0, 50)
t_eval = np.linspace(*t_span, 1000)

# Lösen der Differentialgleichungen
sol = solve_ivp(derivatives, t_span, [theta1_0, omega1_0, theta2_0, omega2_0], t_eval=t_eval)

# Setup für die Animation
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Erstelle die Pendelachsen
line, = ax.plot([], [], 'o-', lw=2)

# Erstelle die Spur des Pendels
trail1, = ax.plot([], [], 'r-', lw=1, alpha=0.5)  # Spur des äußeren Pendels
trail2, = ax.plot([], [], 'g-', lw=1, alpha=0.5)  # Spur des inneren Pendels

# Update-Funktion für die Animation
def update(frame):
    # Pendelkoordinaten berechnen
    x1 = L1 * np.sin(sol.y[0][frame])
    y1 = -L1 * np.cos(sol.y[0][frame])
    x2 = x1 + L2 * np.sin(sol.y[2][frame])
    y2 = y1 - L2 * np.cos(sol.y[2][frame])

    # Aktualisieren der Pendelpositionen
    line.set_data([0, x1, x2], [0, y1, y2])
    
    # Aktualisieren der Spur
    x_trail1 = L1 * np.sin(sol.y[0][:frame])  # Spur des äußeren Pendels
    y_trail1 = -L1 * np.cos(sol.y[0][:frame])
    trail1.set_data(x_trail1, y_trail1)
    
    x_trail2 = x1 + L2 * np.sin(sol.y[2][:frame])  # Spur des inneren Pendels
    y_trail2 = y1 - L2 * np.cos(sol.y[2][:frame])
    trail2.set_data(x_trail2, y_trail2)
    
    return line, trail1, trail2

# Animation erstellen
ani = FuncAnimation(fig, update, frames=len(t_eval), interval=20, blit=True)

plt.show()
