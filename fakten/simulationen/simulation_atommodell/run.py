import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button
from parameters_and_functions import solve_coupled_oscillators, make_interpolators, resonance_condition
from animation import update, init

def main():
    t = np.linspace(0, 50, 4000)
    m = 1.0

    # Initialparameter
    omega1_0 = 2 * np.pi * 1.0
    omega2_0 = 2 * np.pi * 1.02
    k_0 = 0.15

    # Plots und Slider
    axcolor = 'lightgoldenrodyellow'
    fig = plt.figure(figsize=(16, 9))
    ax_traj = plt.subplot2grid((2, 2), (0, 0))
    ax_sin = plt.subplot2grid((2, 2), (0, 1))
    energy_ax = plt.subplot2grid((2, 2), (1, 0), colspan=2)
    plt.subplots_adjust(left=0.07, right=0.98, top=0.93, bottom=0.37, wspace=0.22, hspace=0.32)

    ax_f1 = plt.axes([0.17, 0.28, 0.7, 0.035], facecolor=axcolor)
    ax_f2 = plt.axes([0.17, 0.23, 0.7, 0.035], facecolor=axcolor)
    ax_k = plt.axes([0.17, 0.18, 0.7, 0.035], facecolor=axcolor)
    ax_tol = plt.axes([0.17, 0.13, 0.7, 0.035], facecolor=axcolor)
    ax_speed = plt.axes([0.17, 0.08, 0.7, 0.035], facecolor=axcolor)

    # Frequenz-Slider (Hz), Kopplung
    f1_slider = Slider(ax_f1, 'Frequenz 1 (Hz)', 0.7, 1.3, valinit=1.0, valstep=0.005)
    f2_slider = Slider(ax_f2, 'Frequenz 2 (Hz)', 0.7, 1.3, valinit=1.02, valstep=0.005)
    k_slider = Slider(ax_k, 'Kopplung k', 0.00, 0.50, valinit=k_0, valstep=0.005)
    tol_slider = Slider(ax_tol, 'Toleranz', 0.01, 0.5, valinit=0.1, valstep=0.01)
    speed_slider = Slider(ax_speed, 'Geschwindigkeit', 10, 200, valinit=50, valstep=1)

    # Export-Button
    ax_export = plt.axes([0.82, 0.025, 0.13, 0.045])
    btn_export = Button(ax_export, 'Export Resonanzzeiten', color='lightblue', hovercolor='deepskyblue')

    # Initiale Lösung
    def current_omegas():
        return 2 * np.pi * f1_slider.val, 2 * np.pi * f2_slider.val

    t_num, x1_num, v1_num, x2_num, v2_num = solve_coupled_oscillators(t, *current_omegas(), k_slider.val, m=m)
    x1_interp, v1_interp, x2_interp, v2_interp = make_interpolators(t_num, x1_num, v1_num, x2_num, v2_num)

    # Trajektorien-Plot inkl. Spur
    line1, = ax_traj.plot([], [], 'bo', markersize=8, label='Teilchen 1')
    line2, = ax_traj.plot([], [], 'ro', markersize=8, label='Teilchen 2')
    line1_path, = ax_traj.plot([], [], 'b-', linewidth=0.5, alpha=0.5)
    line2_path, = ax_traj.plot([], [], 'r-', linewidth=0.5, alpha=0.5)
    ax_traj.set_xlim(-1.5, 1.5)
    ax_traj.set_ylim(-1, 1.5)
    ax_traj.set_xlabel("Position")
    ax_traj.set_ylabel("Y-Achse")
    ax_traj.legend(loc='upper left')
    ax_traj.set_title("Trajektorien")

    # Sinusplot
    sinus_line1, = ax_sin.plot([], [], 'b-', label='Teilchen 1 Sinus')
    sinus_line2, = ax_sin.plot([], [], 'r-', label='Teilchen 2 Sinus')
    resonance_line, = ax_sin.plot([], [], 'g|', markersize=15, label='Resonanz')
    ax_sin.set_xlim(t[0], t[-1])
    ax_sin.set_ylim(-1.2, 1.2)
    ax_sin.set_xlabel("Zeit")
    ax_sin.set_ylabel("Amplitude")
    ax_sin.legend(fontsize='small')
    ax_sin.set_title("Sinusverläufe")

    # Energieplot: Farben und Legende nach Empfehlung
    kin_line, = energy_ax.plot([], [], color='blue', label='kinetisch')
    pot_line, = energy_ax.plot([], [], color='orange', label='potenziell')
    coup_line, = energy_ax.plot([], [], color='purple', label='Kopplung')
    tot_line, = energy_ax.plot([], [], color='black', linestyle='--', label='gesamt')
    energy_ax.set_xlim(t[0], t[-1])
    energy_ax.set_ylim(0, 2)
    energy_ax.set_xlabel("Zeit")
    energy_ax.set_ylabel("Energie")
    energy_ax.legend(loc="upper right")
    energy_ax.set_title("Energieverlauf der gekoppelten Oszillatoren")

    # Parameter-Container
    params = {
        'tol_slider': tol_slider,
        'min_resonance_distance': 1.0,
        'omega1': 2 * np.pi * f1_slider.val,
        'omega2': 2 * np.pi * f2_slider.val,
        'k': k_slider.val,
        'm': m
    }

    resonance_history = []

    def wrapped_init():
        resonance_history.clear()
        return init(line1, line2, sinus_line1, sinus_line2, resonance_line, line1_path, line2_path,
                    kin_line, pot_line, coup_line, tot_line, energy_ax)

    # Die Interpolatoren müssen bei jedem Slider-Update neu erzeugt werden!
    def recalc_interpolators():
        nonlocal x1_interp, v1_interp, x2_interp, v2_interp, t_num, x1_num, v1_num, x2_num, v2_num
        params['omega1'] = 2 * np.pi * f1_slider.val
        params['omega2'] = 2 * np.pi * f2_slider.val
        params['k'] = k_slider.val
        t_num, x1_num, v1_num, x2_num, v2_num = solve_coupled_oscillators(
            t, params['omega1'], params['omega2'], params['k'], m=m
        )
        x1_interp, v1_interp, x2_interp, v2_interp = make_interpolators(t_num, x1_num, v1_num, x2_num, v2_num)
        resonance_history.clear()
        # Optional: Energiebilanz prüfen/debug
        from parameters_and_functions import compute_energies
        T, V1, V2, Vc, E = compute_energies(x1_num, v1_num, x2_num, v2_num, params['omega1'], params['omega2'], params['k'], m)
        deltaE = np.max(E) - np.min(E)
        print(f"Delta E: {deltaE:.5e}")

    def update_wrapper(frame, *args):
        return update(
            frame, *args,
            t, x1_interp, v1_interp, x2_interp, v2_interp, ax_traj, ax_sin, resonance_condition,
            params, resonance_history
        )

    ani = FuncAnimation(
        fig,
        update_wrapper,
        frames=len(t),
        init_func=wrapped_init,
        interval=1000 / speed_slider.val,
        blit=True,
        fargs=(
            line1, line2, sinus_line1, sinus_line2, resonance_line, line1_path, line2_path,
            kin_line, pot_line, coup_line, tot_line, energy_ax
        )
    )

    def update_params(val):
        recalc_interpolators()

    def update_speed(val):
        ani.event_source.interval = 1000 / speed_slider.val

    f1_slider.on_changed(update_params)
    f2_slider.on_changed(update_params)
    k_slider.on_changed(update_params)
    tol_slider.on_changed(lambda val: None)
    speed_slider.on_changed(update_speed)

    def on_export(event):
        filename = "resonanzzeiten.csv"
        import csv
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Resonanzzeitpunkt'])
            for t_res in resonance_history:
                writer.writerow([t_res])
        btn_export.label.set_text("Exportiert!")

    btn_export.on_clicked(on_export)

    plt.show()

if __name__ == "__main__":
    main()