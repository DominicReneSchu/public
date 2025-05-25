"""
Doppelpendel – Interaktive Simulation mit Slidern und animierter Spur
© Dominic Schu, 2025 – Alle Rechte vorbehalten.

- Bewegungsgleichungen nach Standardliteratur
- Interaktive Steuerung von Winkeln, Winkelgeschwindigkeiten, Massen und Längen via Slider
- Animation mit Trail (Spur) über die letzten N Frames
- Kapselung des Zustands in einer Klasse
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp
from matplotlib.widgets import Slider

g = 9.81
t_span = (0, 50)
t_steps = 1000
t_eval = np.linspace(*t_span, t_steps)
TRAIL_LENGTH = 200  # Anzahl der Frames, die die Spur sichtbar bleibt

class DoublePendulumSim:
    def __init__(self):
        # Standardwerte
        self.theta1_0 = np.pi / 2
        self.omega1_0 = 0.0
        self.theta2_0 = np.pi / 2
        self.omega2_0 = 0.0
        self.L1 = 1.0
        self.L2 = 1.0
        self.m1 = 1.0
        self.m2 = 1.0
        self.solve()

    def derivatives(self, t, state, m1, m2, L1, L2):
        θ1, ω1, θ2, ω2 = state
        delta = θ2 - θ1

        denom1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta)**2

        dθ1_dt = ω1
        dω1_dt = (m2 * L1 * ω1**2 * np.sin(delta) * np.cos(delta) +
                  m2 * g * np.sin(θ2) * np.cos(delta) +
                  m2 * L2 * ω2**2 * np.sin(delta) -
                  (m1 + m2) * g * np.sin(θ1)) / denom1

        denom2 = (L2 / L1) * denom1

        dθ2_dt = ω2
        dω2_dt = (-m2 * L2 * ω2**2 * np.sin(delta) * np.cos(delta) +
                  (m1 + m2) * g * np.sin(θ1) * np.cos(delta) -
                  (m1 + m2) * L1 * ω1**2 * np.sin(delta) -
                  (m1 + m2) * g * np.sin(θ2)) / denom2

        return [dθ1_dt, dω1_dt, dθ2_dt, dω2_dt]

    def solve(self):
        initial_state = [self.theta1_0, self.omega1_0, self.theta2_0, self.omega2_0]
        self.sol = solve_ivp(
            self.derivatives, t_span, initial_state,
            args=(self.m1, self.m2, self.L1, self.L2),
            t_eval=t_eval, method='RK45'
        )

# --- Hauptprogramm ---
sim = DoublePendulumSim()

fig, ax = plt.subplots(figsize=(7, 7))
plt.subplots_adjust(left=0.1, bottom=0.43)

ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_aspect('equal')
ax.axis('off')

line, = ax.plot([], [], 'o-', lw=2, color='blue')
trail1, = ax.plot([], [], 'r-', lw=1, alpha=0.5)
trail2, = ax.plot([], [], 'g-', lw=1, alpha=0.5)

# --- Slider (Parametersteuerung) ---
axcolor = 'lightgoldenrodyellow'
ax_theta1 = plt.axes([0.1, 0.32, 0.8, 0.03], facecolor=axcolor)
ax_theta2 = plt.axes([0.1, 0.27, 0.8, 0.03], facecolor=axcolor)
ax_omega1 = plt.axes([0.1, 0.22, 0.35, 0.03], facecolor=axcolor)
ax_omega2 = plt.axes([0.55, 0.22, 0.35, 0.03], facecolor=axcolor)
ax_m1 = plt.axes([0.1, 0.17, 0.35, 0.03], facecolor=axcolor)
ax_m2 = plt.axes([0.55, 0.17, 0.35, 0.03], facecolor=axcolor)
ax_L1 = plt.axes([0.1, 0.12, 0.35, 0.03], facecolor=axcolor)
ax_L2 = plt.axes([0.55, 0.12, 0.35, 0.03], facecolor=axcolor)

s_theta1 = Slider(ax_theta1, r'$\theta_1$ (rad)', 0, 2*np.pi, valinit=sim.theta1_0)
s_theta2 = Slider(ax_theta2, r'$\theta_2$ (rad)', 0, 2*np.pi, valinit=sim.theta2_0)
s_omega1 = Slider(ax_omega1, r'$\omega_1$ (rad/s)', -10, 10, valinit=sim.omega1_0)
s_omega2 = Slider(ax_omega2, r'$\omega_2$ (rad/s)', -10, 10, valinit=sim.omega2_0)
s_m1 = Slider(ax_m1, 'm1 (kg)', 0.1, 5.0, valinit=sim.m1)
s_m2 = Slider(ax_m2, 'm2 (kg)', 0.1, 5.0, valinit=sim.m2)
s_L1 = Slider(ax_L1, 'L1 (m)', 0.1, 2.0, valinit=sim.L1)
s_L2 = Slider(ax_L2, 'L2 (m)', 0.1, 2.0, valinit=sim.L2)

ani = None

def get_positions(sol, L1, L2, frame):
    θ1 = sol.y[0][frame]
    θ2 = sol.y[2][frame]
    x1 = L1 * np.sin(θ1)
    y1 = -L1 * np.cos(θ1)
    x2 = x1 + L2 * np.sin(θ2)
    y2 = y1 - L2 * np.cos(θ2)
    return x1, y1, x2, y2

def init():
    line.set_data([], [])
    trail1.set_data([], [])
    trail2.set_data([], [])
    return line, trail1, trail2

def update(frame):
    x1, y1, x2, y2 = get_positions(sim.sol, s_L1.val, s_L2.val, frame)
    line.set_data([0, x1, x2], [0, y1, y2])

    # Trails: Nur die letzten TRAIL_LENGTH Frames anzeigen
    start = max(0, frame - TRAIL_LENGTH)
    x_trail1 = s_L1.val * np.sin(sim.sol.y[0][start:frame])
    y_trail1 = -s_L1.val * np.cos(sim.sol.y[0][start:frame])
    trail1.set_data(x_trail1, y_trail1)

    x_trail2 = (s_L1.val * np.sin(sim.sol.y[0][start:frame]) +
                s_L2.val * np.sin(sim.sol.y[2][start:frame]))
    y_trail2 = (-s_L1.val * np.cos(sim.sol.y[0][start:frame]) -
                s_L2.val * np.cos(sim.sol.y[2][start:frame]))
    trail2.set_data(x_trail2, y_trail2)
    return line, trail1, trail2

def restart_animation(*_):
    global ani
    # Parameter-Update
    sim.theta1_0 = s_theta1.val
    sim.omega1_0 = s_omega1.val
    sim.theta2_0 = s_theta2.val
    sim.omega2_0 = s_omega2.val
    sim.m1 = s_m1.val
    sim.m2 = s_m2.val
    sim.L1 = s_L1.val
    sim.L2 = s_L2.val
    sim.solve()
    # Animation neu starten
    ani.event_source.stop()
    ani._stop()
    start_animation()

def start_animation():
    global ani
    ani = FuncAnimation(fig, update, frames=t_steps, init_func=init, interval=20, blit=True)
    plt.draw()

# --- Slider-Events verbinden ---
s_theta1.on_changed(restart_animation)
s_theta2.on_changed(restart_animation)
s_omega1.on_changed(restart_animation)
s_omega2.on_changed(restart_animation)
s_m1.on_changed(restart_animation)
s_m2.on_changed(restart_animation)
s_L1.on_changed(restart_animation)
s_L2.on_changed(restart_animation)

start_animation()
plt.show()