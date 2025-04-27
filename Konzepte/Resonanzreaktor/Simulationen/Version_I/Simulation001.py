import numpy as np
import matplotlib.pyplot as plt
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Definieren von Parametern
mass = 1.0  # Masse des Teilchens (z.B. Atomkern)
k = 1.0  # Federkonstante (Repräsentation der Wechselwirkung)
damping = 0.05  # Dämpfung des Systems
frequency_resonance = 1.0  # Resonanzfrequenz des Materials
time_step = 0.1  # Zeitschritt
time_end = 100  # Dauer der Simulation

# Zeitbereich
time = np.arange(0, time_end, time_step)

# Anfangsbedingungen
initial_position = 0.5  # Anfangsposition
initial_velocity = 0.0  # Anfangsgeschwindigkeit

# Berechnung der Position und Geschwindigkeit über die Zeit (Dämpfungs-Oszillation)
position = np.zeros_like(time)
velocity = np.zeros_like(time)

position[0] = initial_position
velocity[0] = initial_velocity

for i in range(1, len(time)):
    # Berechnung der Beschleunigung (F = ma, hier als Differentialgleichung)
    force = -k * position[i-1] - damping * velocity[i-1]  # Hooke'sche Gesetz + Dämpfung
    acceleration = force / mass
    
    # Berechnung der neuen Geschwindigkeit und Position
    velocity[i] = velocity[i-1] + acceleration * time_step
    position[i] = position[i-1] + velocity[i] * time_step
    
    # Anregung durch Resonanzfeld: Wenn die Frequenz des Systems der Resonanzfrequenz nahekommt
    if np.abs(np.sin(2 * np.pi * frequency_resonance * time[i])) > 0.5:
        position[i] += 0.1 * np.sin(2 * np.pi * frequency_resonance * time[i])  # Resonanzanregung

# Plot der Ergebnisse
plt.figure(figsize=(10, 6))
plt.plot(time, position, label="Position des Teilchens", color='b')
plt.title('Simulation des Resonanzreaktors')
plt.xlabel('Zeit (s)')
plt.ylabel('Position')
plt.grid(True)
plt.legend()
plt.show()
