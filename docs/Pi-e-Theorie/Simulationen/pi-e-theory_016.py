import numpy as np
import matplotlib.pyplot as plt
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Konstanten
k_B = 1.38e-23  # Boltzmann-Konstante in J/K
hbar = 1.0545718e-34  # Reduziertes Plancksches Wirkungsquantum in J*s
m = 4.65e-26  # Masse eines Atoms (für z.B. Aluminium) in kg
omega_0 = 2 * np.pi * 1e13  # Eigenfrequenz des Systems in Hz
alpha = 1e-10  # Kopplungskonstante in N/m
T = 300  # Temperatur in Kelvin

# Gitterparameter
N = 100  # Anzahl der Atome im Gitter
L = 1e-9  # Länge des Gitters in Metern
dx = L / N  # Abstand zwischen benachbarten Atomen

# Zeit und Amplituden
t = np.linspace(0, 1e-12, 500)  # Zeit in Sekunden
A = np.sin(omega_0 * t)  # Schwingungsamplitude

# Berechnung der Phonon-Frequenzen und Energie
omega = np.linspace(0, 2 * np.pi * 1e13, N)  # Frequenzen der Phononen
omega_t = np.outer(omega, t)  # Erstellen eines 2D-Arrays von Frequenzen und Zeiten

# Schwingungsamplitude für jede Frequenz und Zeit
A_t = np.sin(omega_t)

# Phonon-Energie
phonon_energy = 0.5 * m * omega_t**2 * A_t**2  # Phonon-Energie

# Berechnung der Entropie aus der Bose-Einstein-Verteilung
def bose_einstein_distribution(omega, T):
    return 1 / (np.exp(hbar * omega / (k_B * T)) - 1)

phonon_distribution = bose_einstein_distribution(omega, T)
entropy = k_B * np.sum(phonon_distribution * np.log(phonon_distribution))  # Entropie

# Sicherstellen, dass die Log-Datei erstellt wird
log_file_path = 'log.txt'
try:
    with open(log_file_path, 'w') as log_file:
        log_file.write("Berechnete Phonon-Energie und Entropie\n")
        log_file.write("--------------------------------------------------\n")
        log_file.write(f"Temperatur T: {T} K\n")
        log_file.write(f"Berechnete Entropie des Systems: {entropy:.2e} J/K\n")
        log_file.write("--------------------------------------------------\n")
        log_file.write("Phonon-Energie:\n")
        log_file.write(f"{phonon_energy}\n")
        log_file.write("--------------------------------------------------\n")
        log_file.write("Phonon-Verteilung:\n")
        log_file.write(f"{phonon_distribution}\n")
        log_file.write("--------------------------------------------------\n")
    print(f"Log-Datei erfolgreich erstellt: {log_file_path}")
except Exception as e:
    print(f"Fehler beim Schreiben der Log-Datei: {e}")

# Visualisierung der Phonon-Energie und Entropie
plt.figure(figsize=(12, 6))

# Subplot für Phonon-Energie
plt.subplot(1, 2, 1)
plt.plot(omega, np.mean(phonon_energy, axis=1), label="Phonon-Energie")
plt.title("Phonon-Energie")
plt.xlabel("Frequenz (Hz)")
plt.ylabel("Energie (J)")
plt.legend()

# Subplot für Entropie
plt.subplot(1, 2, 2)
plt.plot(omega, phonon_distribution, label="Phonon-Verteilung")
plt.title(f"Phonon-Verteilung und Entropie: {entropy:.2e} J/K")
plt.xlabel("Frequenz (Hz)")
plt.ylabel("Bose-Einstein-Verteilung")
plt.legend()

plt.tight_layout()
plt.show()

print(f"Berechnete Entropie des Systems: {entropy:.2e} J/K")
