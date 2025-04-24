import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Zeitachse
t = np.linspace(0, 10, 1000)

# Frequenzen
f_pi = np.pi
f_e = np.e

# Vorberechnung der Einzelsignale
signal_pi = np.sin(2 * np.pi * f_pi * t)
signal_e = np.sin(2 * np.pi * f_e * t)

# Initialer Bewusstseinsfaktor
alpha_init = 0.5

# Gleitender Mittelwert-Funktion
def moving_average(data, window):
    return np.convolve(data, np.ones(window)/window, mode='same')

# Initiales Signal
def compute(alpha):
    signal = signal_pi + alpha * signal_e
    energy = signal**2
    entropy = moving_average(energy, 50)
    return signal, energy, entropy

# Initialdaten berechnen
signal, energy, entropy = compute(alpha_init)

# Plot vorbereiten
fig, axs = plt.subplots(3, 1, figsize=(12, 8))
plt.subplots_adjust(bottom=0.25)

l1, = axs[0].plot(t, signal, label='π + α·e Resonanz', color='blue')
axs[0].set_ylabel('Amplitude')
axs[0].legend()
axs[0].grid(True)

l2, = axs[1].plot(t, energy, label='Energie (Amplitude²)', color='red')
axs[1].set_ylabel('Energie')
axs[1].legend()
axs[1].grid(True)

l3, = axs[2].plot(t, entropy, label='Strukturentropie (Pseudo)', color='green')
axs[2].set_ylabel('Strukturentropie')
axs[2].set_xlabel('Zeit')
axs[2].legend()
axs[2].grid(True)

# Slider einfügen
ax_alpha = plt.axes([0.25, 0.05, 0.5, 0.03])
slider_alpha = Slider(ax_alpha, 'α (Bewusstsein)', 0.0, 1.0, valinit=alpha_init)

# Update-Funktion
def update(val):
    alpha = slider_alpha.val
    signal, energy, entropy = compute(alpha)
    l1.set_ydata(signal)
    l2.set_ydata(energy)
    l3.set_ydata(entropy)
    fig.canvas.draw_idle()

slider_alpha.on_changed(update)

plt.show()
