import numpy as np
import matplotlib.pyplot as plt

# Konstanten
A = 14      # Maximale Sonneneinstrahlung in Watt/m² (vereinfachte Annahme)
T0 = 5      # Anfangstemperatur am Morgen (°C)
k = 0.3     # Temperatursteigerungsfaktor (Wirkung der Sonneneinstrahlung)
phi = 0     # Phasenverschiebung der Sonneneinstrahlung (angepasst an den Sonnenaufgang)
wind_speed_mean = 10  # Durchschnittliche Windgeschwindigkeit (km/h)
humidity_base = 60    # Basis-Luftfeuchtigkeit

# Zusätzliche Parameter für die Schu-Gleichung
epsilon = 8.85e-12  # Die Permittivität des Vakuums (F/m)
h = 6.626e-34       # Plancksches Wirkungsquantum (J·s)
alpha = np.pi / 4   # Ein Beispielwert für den Winkel alpha (45° in Radiant)
f_real = 1.0        # Realer Teil der Frequenz
f_imag = 0.5        # Imaginärer Teil der Frequenz

# Zeitspanne des Tages (06:00 bis 20:30 Uhr)
time_hours = np.arange(6, 21, 1)  # 6:00 bis 20:00 Uhr in 1-Stunden-Schritten

# Berechnung der Sonneneinstrahlung basierend auf einer Sinuskurve
def solar_irradiance(t):
    return A * np.sin((2 * np.pi / 24) * (t - 6) + phi)

# Berechnung der Temperatur in Abhängigkeit von der Sonneneinstrahlung
def temperature(t):
    return T0 + k * solar_irradiance(t)

# Berechnung der Windgeschwindigkeit (bleibt konstant mit leichten Schwankungen)
def wind_speed(t):
    return wind_speed_mean + np.random.uniform(-2, 2)  # Schwankungen um ±2 km/h

# Berechnung der Luftfeuchtigkeit
def humidity(t):
    return humidity_base + (temperature(t) - 5) * 1.5  # Luftfeuchtigkeit steigt mit Temperatur

# Berechnung der Niederschlagswahrscheinlichkeit basierend auf der Temperatur
def precipitation_probability(t):
    temperature_value = temperature(t)
    
    # Angenommene Formel: Wenn die Temperatur unter 10°C liegt, steigt die Wahrscheinlichkeit für Niederschlag
    if temperature_value < 10:
        return np.random.uniform(0.4, 0.7)  # 40% bis 70% Wahrscheinlichkeit für Niederschlag
    elif temperature_value > 30:
        return np.random.uniform(0.2, 0.4)  # 20% bis 40% Wahrscheinlichkeit für Niederschlag
    else:
        return np.random.uniform(0.1, 0.3)  # 10% bis 30% Wahrscheinlichkeit für Niederschlag

# Berechnung der Schu-Gleichung (E)
def schu_equation():
    E = np.pi * epsilon * h * (np.cos(alpha) * f_real + 1j * np.sin(alpha) * f_imag)
    return E

# Berechnungen für den gesamten Tagesverlauf
temperatures = [temperature(t) for t in time_hours]
winds = [wind_speed(t) for t in time_hours]
humidities = [humidity(t) for t in time_hours]
precipitations = [precipitation_probability(t) for t in time_hours]

# Berechnung der Schu-Gleichung für den Tag
E = schu_equation()

# Visualisierung des Tagesverlaufs
plt.figure(figsize=(10, 6))

# Temperaturverlauf
plt.subplot(3, 1, 1)
plt.plot(time_hours, temperatures, label="Temperatur (°C)", color='orange')
plt.title("Tagesverlauf am 26. April 2025 in Zeven")
plt.xlabel("Uhrzeit")
plt.ylabel("Temperatur (°C)")
plt.grid(True)

# Windgeschwindigkeit
plt.subplot(3, 1, 2)
plt.plot(time_hours, winds, label="Windgeschwindigkeit (km/h)", color='blue')
plt.xlabel("Uhrzeit")
plt.ylabel("Windgeschwindigkeit (km/h)")
plt.grid(True)

# Luftfeuchtigkeit
plt.subplot(3, 1, 3)
plt.plot(time_hours, humidities, label="Luftfeuchtigkeit (%)", color='green')
plt.xlabel("Uhrzeit")
plt.ylabel("Luftfeuchtigkeit (%)")
plt.grid(True)

plt.tight_layout()
plt.show()

# Ausgabe der Schu-Gleichung
print(f"Schu-Gleichung E: {E}")
# Ausgabe der Stundenwerte für Temperatur, Windgeschwindigkeit und Luftfeuchtigkeit
print(f"{'Uhrzeit (h)':<15} {'Temperatur (°C)':<20} {'Windgeschwindigkeit (km/h)':<30} {'Luftfeuchtigkeit (%)':<20}")
print("-" * 85)

# Iteriere durch die Zeit und gebe die berechneten Werte aus
for t in time_hours:
    temp = temperature(t)
    wind = wind_speed(t)
    humidity_value = humidity(t)
    print(f"{t:<15.1f} {temp:<20.2f} {wind:<30.2f} {humidity_value:<20.2f}")
