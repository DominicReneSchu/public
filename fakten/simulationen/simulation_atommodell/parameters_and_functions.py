import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

def coupled_oscillators(t, y, omega1, omega2, k, m):
    x1, v1, x2, v2 = y
    dx1dt = v1
    dv1dt = -omega1**2 * x1 + (k/m)*(x2 - x1)
    dx2dt = v2
    dv2dt = -omega2**2 * x2 + (k/m)*(x1 - x2)
    return [dx1dt, dv1dt, dx2dt, dv2dt]

def solve_coupled_oscillators(t_grid, omega1, omega2, k, m=1.0, y0=None):
    if y0 is None:
        y0 = [1.0, 0.0, 0.0, 0.0]
    sol = solve_ivp(
        lambda t, y: coupled_oscillators(t, y, omega1, omega2, k, m),
        (t_grid[0], t_grid[-1]), y0, t_eval=t_grid, rtol=1e-8, atol=1e-10
    )
    return sol.t, sol.y[0], sol.y[1], sol.y[2], sol.y[3]  # t, x1, v1, x2, v2

def make_interpolators(t, x1, v1, x2, v2):
    x1i = interp1d(t, x1, kind='cubic', bounds_error=False, fill_value="extrapolate")
    v1i = interp1d(t, v1, kind='cubic', bounds_error=False, fill_value="extrapolate")
    x2i = interp1d(t, x2, kind='cubic', bounds_error=False, fill_value="extrapolate")
    v2i = interp1d(t, v2, kind='cubic', bounds_error=False, fill_value="extrapolate")
    return x1i, v1i, x2i, v2i

def resonance_condition(x1, x2, tolerance=0.1):
    return np.abs(x1 - x2) < tolerance

def compute_energies(x1, v1, x2, v2, omega1, omega2, k, m=1.0):
    # Kinetische Energie
    T = 0.5*m*v1**2 + 0.5*m*v2**2
    # Potentielle Energie beider Federn
    V1 = 0.5*m*omega1**2*x1**2
    V2 = 0.5*m*omega2**2*x2**2
    # Kopplungsenergie
    Vc = 0.5*k*(x1 - x2)**2
    # Gesamtenergie
    E = T + V1 + V2 + Vc
    return T, V1, V2, Vc, E