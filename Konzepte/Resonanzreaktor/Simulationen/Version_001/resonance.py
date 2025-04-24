# resonance.py
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
import numpy as np

def resonance_field(frequency, temperature):
    """Berechnet das Resonanzfeld unter Berücksichtigung der Temperatur."""
    adjusted_frequency = frequency * (1 + 0.01 * (temperature - 300))  # Temperaturabhängigkeit
    resonance_window = 0.1 * adjusted_frequency  # Breite des Resonanzfensters
    return adjusted_frequency, resonance_window

def excite_material(material, time, temperature):
    """Berechnet die Anregung des Materials basierend auf der Resonanzfrequenz und Zeit."""
    decay_effect = material.decay(time)
    resonance_freq, resonance_window = resonance_field(material.resonance_freq, temperature)
    
    # Modifizierte Anregung, abhängig vom Zerfall des Materials und der Resonanzfrequenz
    excitation_level = np.sin(resonance_freq * time) * decay_effect  # Einfache Schwingungsberechnung
    return excitation_level, resonance_window
