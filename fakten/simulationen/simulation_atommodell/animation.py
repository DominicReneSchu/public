import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# Parameter für die Simulation
t = np.linspace(0, 10, 1000)
x1, x2 = np.sin(t), np.cos(t)

# Hauptplot-Fenster und Teilchen-Darstellung
fig1, ax1 = plt.subplots()
line1, = ax1.plot([], [], 'bo', markersize=8, label='Teilchen 1')
line2, = ax1.plot([], [], 'ro', markersize=8, label='Teilchen 2')
ax1.set(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), xlabel="X-Achse", ylabel="Y-Achse")
ax1.legend()

# Zusätzliche Darstellung der Sinus-Verläufe
fig2, ax2 = plt.subplots()
sinus_line1, = ax2.plot([], [], 'b-', label='Teilchen 1 Sinus')
sinus_line2, = ax2.plot([], [], 'r-', label='Teilchen 2 Sinus')
ax2.set(xlim=(0, 10), ylim=(-1.2, 1.2), xlabel="Zeit", ylabel="Amplitude")
ax2.legend()

def update(frame, line1, line2, sinus_line1, sinus_line2):
    """Aktualisiert die Positionen der Teilchen und deren Sinus-Verläufe."""
    line1.set_data(x1[:frame], np.zeros_like(x1[:frame]))
    line2.set_data(x2[:frame], np.zeros_like(x2[:frame]))
    sinus_line1.set_data(t[:frame], x1[:frame])
    sinus_line2.set_data(t[:frame], x2[:frame])
    return line1, line2, sinus_line1, sinus_line2

def init():
    """Initialisiert die Daten für die Animation."""
    for line in (line1, line2, sinus_line1, sinus_line2):
        line.set_data([], [])
    return line1, line2, sinus_line1, sinus_line2

# Schieberegler für die Geschwindigkeit
ax_slider = plt.axes([0.25, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')
speed_slider = Slider(ax_slider, 'Geschwindigkeit', 10, 200, valinit=50, valstep=1)

def update_speed(val):
    """Ändert die Geschwindigkeit der Animation basierend auf dem Slider-Wert."""
    ani.event_source.interval = 1000 / speed_slider.val

speed_slider.on_changed(update_speed)

# Animation initialisieren
ani = FuncAnimation(
    fig1, 
    update, 
    frames=len(t), 
    init_func=init, 
    interval=1000 / speed_slider.val, 
    blit=True,
    fargs=(line1, line2, sinus_line1, sinus_line2)
)

plt.show()