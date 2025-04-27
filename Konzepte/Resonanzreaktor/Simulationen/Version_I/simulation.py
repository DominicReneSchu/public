# simulation.py
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
import numpy as np
import matplotlib.pyplot as plt
from material import uranium_235, plutonium_239, thorium_232
from resonance import excite_material

def run_simulation(material, time_steps, temperature):
    time = np.linspace(0, time_steps, time_steps)
    excitation_levels = []

    for t in time:
        excitation, window = excite_material(material, t, temperature)
        excitation_levels.append(excitation)

    return time, excitation_levels

def plot_results(time, excitation_levels):
    plt.figure()
    plt.plot(time, excitation_levels)
    plt.title('Resonanzanregung des Materials')
    plt.xlabel('Zeit (s)')
    plt.ylabel('Exzitationslevel')
    plt.show()

if __name__ == "__main__":
    time_steps = 1000
    temperature = 350  # Beispielhafte Temperatur in Kelvin
    material = uranium_235  # Beispiel für Uranium-235

    time, excitation_levels = run_simulation(material, time_steps, temperature)
    plot_results(time, excitation_levels)
