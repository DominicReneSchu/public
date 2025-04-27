# material.py
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
import numpy as np

# Basis-Isotopenklasse
class Isotope:
    def __init__(self, name, half_life, resonance_freq, decay_constant, energy_per_decay=None):
        """
        Erstellt eine Instanz eines Isotops mit den gegebenen Eigenschaften.
        
        Args:
            name (str): Name des Isotops.
            half_life (float): Halbwertszeit in Jahren.
            resonance_freq (float): Resonanzfrequenz in Hz.
            decay_constant (float): Zerfallskonstante in 1/Jahr.
            energy_per_decay (float, optional): Energie pro Zerfall in MeV.
        """
        self.name = name
        self.half_life = half_life
        self.resonance_freq = resonance_freq
        self.decay_constant = decay_constant
        self.energy_per_decay = energy_per_decay

    def decay(self, time):
        """Berechnet den Zerfall des Materials über eine gegebene Zeitspanne."""
        return np.exp(-self.decay_constant * time)  # Exponentieller Zerfall

    def energy_released(self, time):
        """Berechnet die freigesetzte Energie über eine gegebene Zeitspanne."""
        if self.energy_per_decay is not None:
            decay_factor = self.decay(time)
            return decay_factor * self.energy_per_decay
        else:
            return 0  # Wenn keine Energie pro Zerfall definiert wurde

# Beispiele für Isotope mit Energiefreigabe
uranium_235 = Isotope("Uranium-235", 700000000, 1.5e8, 0.0001, energy_per_decay=200)  # Beispielenergie in MeV
plutonium_239 = Isotope("Plutonium-239", 24000, 2.1e8, 0.0002, energy_per_decay=200)
thorium_232 = Isotope("Thorium-232", 1400000000, 1.8e8, 0.00005, energy_per_decay=100)  # Beispielenergie in MeV

# Erweiterung: Transmutierte Isotope
americium_241 = Isotope("Americium-241", 432, 1.9e8, 0.00015, energy_per_decay=5.5)