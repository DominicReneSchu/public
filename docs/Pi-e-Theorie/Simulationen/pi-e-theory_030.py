import numpy as np
import matplotlib.pyplot as plt

# Definiere die Parameter für das System
omega_0 = 2 * np.pi  # Eigenfrequenz des Systems (z. B. Resonanzfrequenz)
gamma = 0.1          # Dämpfungskoeffizient
A = np.linspace(0, 1, 500)  # Amplitudenbereich
omega_ext = np.linspace(omega_0 - 5, omega_0 + 5, 500)  # Externe Frequenzen

# Erzeuge ein Meshgrid für die Berechnung
A_grid, omega_ext_grid = np.meshgrid(A, omega_ext)

# Berechne die Resonanzenergie als 2D-Matrix
E_resonance = 1 / (1 + ((omega_ext_grid - omega_0) / gamma)**2)

# Berechne die Entropie
# Vermeide log(0) durch Maskieren der Werte, die null sind.
E_resonance[E_resonance == 0] = np.nan  # Setze Nullwerte auf NaN, um Fehler zu vermeiden
entropy = -np.sum(E_resonance * np.log(E_resonance), axis=1)  # Entropie über Amplituden

# Visualisierung der Resonanzenergie und Entropie
fig = plt.figure(figsize=(10, 6))

# Subplot 1: Resonanzenergie
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(omega_ext_grid, A_grid, E_resonance, cmap='inferno', edgecolor='none')
ax1.set_xlabel('Resonanzfrequenz (Hz)')
ax1.set_ylabel('Amplitude')
ax1.set_zlabel('Resonanzenergie')
ax1.set_title('Resonanzenergie in Abhängigkeit von Frequenz und Amplitude')

# Subplot 2: Entropie
ax2 = fig.add_subplot(122)
ax2.plot(omega_ext, entropy)
ax2.set_xlabel('Resonanzfrequenz (Hz)')
ax2.set_ylabel('Entropie')
ax2.set_title('Entropie in Abhängigkeit von der Resonanzfrequenz')

# Layout anpassen und Plot anzeigen
plt.tight_layout()
plt.show()

# Warten auf Benutzerinput, um das Fenster offen zu halten
input("Drücke Enter zum Beenden...")
