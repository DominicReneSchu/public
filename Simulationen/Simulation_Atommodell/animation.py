import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# Parametrisierung der Bewegung (Beispiel)
t = np.linspace(0, 10, 1000)
x1 = np.sin(t)
x2 = np.cos(t)

# Erstelle das Hauptplot-Fenster
fig1, ax1 = plt.subplots()
line1, = ax1.plot([], [], 'bo', markersize=8, label='Teilchen 1')
line2, = ax1.plot([], [], 'ro', markersize=8, label='Teilchen 2')
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)

# Erstelle das Diagramm für die Sinus-Verläufe
fig2, ax2 = plt.subplots()
sinus_line1, = ax2.plot([], [], 'b-', label='Teilchen 1 Sinus')
sinus_line2, = ax2.plot([], [], 'r-', label='Teilchen 2 Sinus')
ax2.set_xlim(0, 10)
ax2.set_ylim(-1.2, 1.2)

# Funktions-Update für Animation
def update(frame, line1, line2, sinus_line1, sinus_line2):
    # Update der Positionen der Teilchen (nur die aktuell angezeigten)
    line1.set_data(x1[:frame], np.zeros_like(x1[:frame]))  # Teilchen 1
    line2.set_data(x2[:frame], np.zeros_like(x2[:frame]))  # Teilchen 2
    # Update der Sinus-Verläufe
    sinus_line1.set_data(t[:frame], x1[:frame])  # Sinus Verlauf für Teilchen 1
    sinus_line2.set_data(t[:frame], x2[:frame])  # Sinus Verlauf für Teilchen 2
    return line1, line2, sinus_line1, sinus_line2

# Initialisiere die Animation
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    sinus_line1.set_data([], [])
    sinus_line2.set_data([], [])
    return line1, line2, sinus_line1, sinus_line2

# Füge Schieberegler für Geschwindigkeit ein
ax_slider = plt.axes([0.25, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')
speed_slider = Slider(ax_slider, 'Geschwindigkeit', 10, 200, valinit=50, valstep=1)

# Funktion, um den Intervall der Animation dynamisch zu ändern
def update_speed(val):
    ani.event_source.interval = 1000 / speed_slider.val  # Geschwindigkeit in Bezug auf den Slider-Wert

# Setze die Callback-Funktion für den Schieberegler
speed_slider.on_changed(update_speed)

# Initialisiere die Animation
ani = FuncAnimation(
    fig1, 
    update, 
    frames=len(t), 
    init_func=init, 
    interval=50, 
    blit=True,
    fargs=(line1, line2, sinus_line1, sinus_line2)  # Hier werden die Argumente übergeben
)

plt.show()
