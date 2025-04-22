import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def doppelpendel(t, y, L1=1.0, L2=1.0, m1=1.0, m2=1.0, g=9.81):
    θ1, ω1, θ2, ω2 = y
    dθ1dt = ω1
    dω1dt = (-g * (2 * m1 + m2) * np.sin(θ1) - m2 * g * np.sin(θ1 - 2 * θ2) 
             - 2 * np.sin(θ1 - θ2) * m2 * (ω2**2 * L2 + ω1**2 * L1 * np.cos(θ1 - θ2))) / (L1 * (2 * m1 + m2 - m2 * np.cos(2 * θ1 - 2 * θ2)))
    dθ2dt = ω2
    dω2dt = (2 * np.sin(θ1 - θ2) * (ω1**2 * L1 * (m1 + m2) + g * (m1 + m2) * np.cos(θ1) 
                                   + ω2**2 * L2 * m2 * np.cos(θ1 - θ2))) / (L2 * (2 * m1 + m2 - m2 * np.cos(2 * θ1 - 2 * θ2)))
    return [dθ1dt, dω1dt, dθ2dt, dω2dt]

# Startwerte (θ1, ω1, θ2, ω2)
initial_conditions = [np.pi / 2, 0, np.pi / 2, 0]

# Längerer Zeitbereich der Simulation
t_span = (0, 100)  # 100 Sekunden statt 10 Sekunden
t_eval = np.linspace(*t_span, 10000)  # Beibehalten der gleichen Anzahl an Auswertungspunkten

# Lösen der Differentialgleichung
sol = solve_ivp(doppelpendel, t_span, initial_conditions, t_eval=t_eval, method='RK45')

# Nulldurchgänge von θ₁ (mit Hysterese für Stabilität)
threshold = 0.001  # Schwellenwert für Hysterese etwas niedriger setzen
crossings = np.where((sol.y[0][:-1] < -threshold) & (sol.y[0][1:] >= threshold))[0]

# Poincaré-Schnitt plotten
if len(crossings) > 0:  # Überprüfen, ob Kreuzungen existieren
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(sol.y[2][crossings], sol.y[3][crossings], 
                          c=sol.t[crossings], cmap='viridis', s=5, alpha=0.6)
    plt.colorbar(scatter, label='Zeit (s)')
    plt.xlabel(r'$\theta_2$ (rad)')
    plt.ylabel(r'$\omega_2$ (rad/s)')
    plt.title('Poincaré-Schnitt: $\theta_1 = 0$ mit $\dot{\theta}_1 > 0$')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("Keine Kreuzungen gefunden!")
