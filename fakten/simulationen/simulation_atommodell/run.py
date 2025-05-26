import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from parameters_and_functions import x1, x2
from animation import update, init

# Hauptfunktion für das Programm
def main():
    # Parameter
    t = np.linspace(0, 10, 1000)

    # Setup der Animation
    fig, ax = plt.subplots()
    line1, = ax.plot([], [], 'bo', markersize=8, label='Teilchen 1')
    line2, = ax.plot([], [], 'ro', markersize=8, label='Teilchen 2')

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.legend()

    # Geschwindigkeit-Schieberegler
    speed_ax = plt.axes([0.25, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    speed_slider = Slider(speed_ax, 'Geschwindigkeit', 10, 200, valinit=50, valstep=1)

    def update_speed(val):
        ani.event_source.interval = 1000 / speed_slider.val

    speed_slider.on_changed(update_speed)

    # Initialisiere Animation
    ani = FuncAnimation(
        fig,
        update,
        frames=len(t),
        init_func=init,
        interval=50,
        blit=True,
        fargs=(line1, line2, t, x1, x2)
    )

    plt.show()

if __name__ == "__main__":
    main()