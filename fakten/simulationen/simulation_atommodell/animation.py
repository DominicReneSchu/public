import numpy as np

def init(line1, line2, sinus_line1, sinus_line2, resonance_line, line1_path, line2_path,
         kin_line, pot_line, coup_line, tot_line, energy_ax):
    for line in (line1, line2, sinus_line1, sinus_line2, line1_path, line2_path,
                 kin_line, pot_line, coup_line, tot_line):
        line.set_data([], [])
    resonance_line.set_data([], [])
    energy_ax.set_ylim(0, 2)  # Startwert, wird dynamisch angepasst
    return (line1, line2, sinus_line1, sinus_line2, resonance_line,
            line1_path, line2_path, kin_line, pot_line, coup_line, tot_line)

def update(
    frame,
    line1, line2, sinus_line1, sinus_line2, resonance_line, line1_path, line2_path,
    kin_line, pot_line, coup_line, tot_line, energy_ax,
    t, x1_interp, v1_interp, x2_interp, v2_interp, ax_traj, ax_sin, resonance_condition_func,
    params, resonance_history
):
    tolerance_slider = params.get('tol_slider')
    tolerance = tolerance_slider.val if hasattr(tolerance_slider, 'val') else params.get('tolerance', 0.1)
    min_dist = params.get('min_resonance_distance', 1.0)
    omega1 = params['omega1']
    omega2 = params['omega2']
    k = params['k']
    m = params.get('m', 1.0)

    t_now = t[frame]
    x1_vals = x1_interp(t[:frame+1])
    v1_vals = v1_interp(t[:frame+1])
    x2_vals = x2_interp(t[:frame+1])
    v2_vals = v2_interp(t[:frame+1])
    x1_now = x1_vals[-1]
    x2_now = x2_vals[-1]

    line1.set_data([x1_now], [0])
    line2.set_data([x2_now], [0.5])
    line1_path.set_data(x1_vals, np.zeros_like(x1_vals))
    line2_path.set_data(x2_vals, np.full_like(x2_vals, 0.5))
    sinus_line1.set_data(t[:frame+1], x1_vals)
    sinus_line2.set_data(t[:frame+1], x2_vals)

    # Resonanzbedingung mit Dopplungsschutz
    resonance_triggered = False
    if frame > 0 and resonance_condition_func(x1_now, x2_now, tolerance):
        if (not resonance_history) or ((t_now - resonance_history[-1]) >= min_dist):
            resonance_history.append(t_now)
            resonance_triggered = True

    # Visuelles Aufleuchten
    if not hasattr(ax_traj, "_highlight_count"):
        ax_traj._highlight_count = 0
    if resonance_triggered:
        ax_traj._highlight_count = 8
    if ax_traj._highlight_count > 0:
        ax_traj.set_facecolor("lightyellow")
        ax_traj._highlight_count -= 1
    else:
        ax_traj.set_facecolor("white")

    # Titel
    if resonance_triggered:
        ax_traj.set_title("Resonanz erreicht! Kopplung aktiv.", color="green")
        ax_sin.set_title(f"Resonanz: t={t_now:.2f}", color="green")
    else:
        ax_traj.set_title("Warten auf Resonanz...", color="red")
        ax_sin.set_title("Sinusverläufe", color="black")

    # Resonanz-Markierungen im Sinusplot
    if resonance_history:
        resonance_line.set_data(resonance_history, [0]*len(resonance_history))
    else:
        resonance_line.set_data([], [])

    # Energieplot
    from parameters_and_functions import compute_energies
    T, V1, V2, Vc, E = compute_energies(x1_vals, v1_vals, x2_vals, v2_vals, omega1, omega2, k, m)
    kin_line.set_data(t[:frame+1], T)
    pot_line.set_data(t[:frame+1], V1 + V2)
    coup_line.set_data(t[:frame+1], Vc)
    tot_line.set_data(t[:frame+1], E)
    # Dynamische Y-Achsen-Anpassung
    max_E = np.max(E)
    energy_ax.set_ylim(0, max(1.2*max_E, 1.2))

    return (line1, line2, sinus_line1, sinus_line2, resonance_line,
            line1_path, line2_path, kin_line, pot_line, coup_line, tot_line)