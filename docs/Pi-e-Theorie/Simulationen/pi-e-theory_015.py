import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Systemparameter für ungedämpftes Pendel
omega_0 = 2 * np.pi  # Eigenfrequenz des Systems
gamma = 0            # Kein Dämpfungsfaktor
theta_0 = 1           # Anfangswinkel
omega_0_dot = 0       # Anfangsgeschwindigkeit

# Differentialgleichung für das ungedämpfte Pendel
def undamped_oscillator(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -omega_0**2 * theta
    return [dtheta_dt, domega_dt]

# Zeitbereich
t_span = (0, 10)
t_eval = np.linspace(0, 10, 1000)

# Anfangsbedingungen: [theta_0, omega_0_dot]
initial_conditions = [theta_0, omega_0_dot]

# Lösung der Differentialgleichung
sol = solve_ivp(undamped_oscillator, t_span, initial_conditions, t_eval=t_eval)

# Energie des Systems
kinetic_energy = 0.5 * sol.y[1]**2  # Kinetische Energie
potential_energy = 0.5 * omega_0**2 * sol.y[0]**2  # Potentielle Energie
total_energy = kinetic_energy + potential_energy  # Gesamte Energie

# Entropie (logarithmisch auf Basis der Gesamtenergie)
entropy = np.log(total_energy + 1e-5)  # Vermeidet den Logarithmus von 0

# Plot der Ergebnisse
plt.figure(figsize=(12, 8))

# Plot der Schwingung (Winkel)
plt.subplot(3, 1, 1)
plt.plot(sol.t, sol.y[0], label="Winkel θ(t)")
plt.title("Schwingung des ungedämpften Pendels")
plt.xlabel("Zeit (s)")
plt.ylabel("Winkel (rad)")
plt.grid(True)
plt.legend()

# Plot der Gesamtenergie
plt.subplot(3, 1, 2)
plt.plot(sol.t, total_energy, label="Gesamtenergie")
plt.title("Gesamtenergie des Systems (ungedämpft)")
plt.xlabel("Zeit (s)")
plt.ylabel("Energie (J)")
plt.grid(True)
plt.legend()

# Plot der Entropie
plt.subplot(3, 1, 3)
plt.plot(sol.t, entropy, label="Entropie", color='red')
plt.title("Entropie des Systems (ungedämpft)")
plt.xlabel("Zeit (s)")
plt.ylabel("Entropie (log)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
