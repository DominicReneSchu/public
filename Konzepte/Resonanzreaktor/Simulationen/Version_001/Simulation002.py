import numpy as np
import matplotlib.pyplot as plt

# Parameter für den Atommüll (z.B. Uran)
N0 = 1e12  # Anfangszahl der Teilchen
lambda_ = 1e-4  # Zerfallskonstante (je kleiner, desto langsamer der Zerfall)
resonance_frequency = 0.01  # Resonanzfrequenz des Materials (in Hz)
temperature = 300  # Temperatur in Kelvin (führt zu einer Breitenänderung des Resonanzfensters)
time = np.linspace(0, 1000, 10000)  # Zeitspanne (in Sekunden)

# Zerfallsgleichung für den radioaktiven Stoff
def radioactive_decay(t, N0, lambda_):
    return N0 * np.exp(-lambda_ * t)

# Resonanzfeld: Einfache Annäherung einer Sinuskurve
def resonance_field(t, resonance_frequency, temperature):
    # Temperatur beeinflusst die Resonanzfrequenz (z.B. breiteres Fenster bei höherer Temperatur)
    resonance_window = resonance_frequency * (1 + 0.01 * (temperature - 300))  
    return np.sin(2 * np.pi * resonance_window * t)

# Berechnung der verbleibenden Teilchenzahl
remaining_particles = radioactive_decay(time, N0, lambda_)

# Berechnung der Resonanzanregung
resonance_effect = resonance_field(time, resonance_frequency, temperature)

# Gesamtenergie: Die Energie des Systems wird als Produkt der verbleibenden Teilchenzahl und der Resonanzanregung berechnet
total_energy = remaining_particles * (1 + 0.5 * resonance_effect)  # Resonanz verstärkt die Energie

# Plotting der Ergebnisse
plt.figure(figsize=(12, 6))

# Position des Teilchens im Zeitverlauf
plt.subplot(2, 1, 1)
plt.plot(time, remaining_particles, label='Verbleibende Teilchen (Zerfall)', color='blue')
plt.xlabel('Zeit (s)')
plt.ylabel('Teilchenzahl')
plt.legend()
plt.title('Zerfall des Atommülls im Zeitverlauf')

# Gesamtenergie (Zerfall + Resonanz)
plt.subplot(2, 1, 2)
plt.plot(time, total_energy, label='Gesamtenergie (Zerfall + Resonanz)', color='red')
plt.xlabel('Zeit (s)')
plt.ylabel('Energie')
plt.legend()
plt.title('Gesamtenergie des Atommülls mit Resonanzanregung')

plt.tight_layout()
plt.show()
