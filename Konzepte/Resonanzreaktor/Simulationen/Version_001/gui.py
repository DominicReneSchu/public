# gui.py

import tkinter as tk
from tkinter import ttk
from simulation import run_simulation, plot_results
from material import uranium_235

def start_simulation():
    material = uranium_235
    time_steps = int(time_steps_entry.get())
    temperature = float(temperature_entry.get())
    
    time, excitation_levels = run_simulation(material, time_steps, temperature)
    plot_results(time, excitation_levels)

root = tk.Tk()
root.title("Resonanzfeld-Simulation")

# UI-Komponenten
ttk.Label(root, text="Zeit-Schritte").grid(row=0, column=0)
time_steps_entry = ttk.Entry(root)
time_steps_entry.grid(row=0, column=1)

ttk.Label(root, text="Temperatur (K)").grid(row=1, column=0)
temperature_entry = ttk.Entry(root)
temperature_entry.grid(row=1, column=1)

start_button = ttk.Button(root, text="Simulation starten", command=start_simulation)
start_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
