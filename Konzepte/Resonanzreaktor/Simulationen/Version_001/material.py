# material.py

class Isotope:
    def __init__(self, name, half_life, resonance_freq, decay_constant):
        self.name = name
        self.half_life = half_life  # Halbwertszeit in Jahren
        self.resonance_freq = resonance_freq  # Resonanzfrequenz in Hz
        self.decay_constant = decay_constant  # Zerfallskonstante in 1/Jahr

    def decay(self, time):
        """Berechnet den Zerfall des Materials über eine gegebene Zeitspanne."""
        return np.exp(-self.decay_constant * time)  # Exponentieller Zerfall

# Beispiele für Isotope:
uranium_235 = Isotope("Uranium-235", 700000000, 1.5e8, 0.0001)
plutonium_239 = Isotope("Plutonium-239", 24000, 2.1e8, 0.0002)
thorium_232 = Isotope("Thorium-232", 1400000000, 1.8e8, 0.00005)
