import numpy as np

def update(frame, scatter1, scatter2, ax, t, x1, x2, resonance_condition):
    """
    Aktualisiert die Positionen der Teilchen und überprüft Resonanzbedingungen.

    Args:
        frame (int): Der aktuelle Frame der Animation.
        scatter1 (matplotlib.collections.PathCollection): Scatter-Punkt für Teilchen 1.
        scatter2 (matplotlib.collections.PathCollection): Scatter-Punkt für Teilchen 2.
        ax (matplotlib.axes.Axes): Achse der Animation.
        t (numpy.ndarray): Zeitpunkte für die Simulation.
        x1 (function): Funktion zur Berechnung der Position von Teilchen 1.
        x2 (function): Funktion zur Berechnung der Position von Teilchen 2.
        resonance_condition (function): Funktion, die überprüft, ob Resonanzbedingungen erfüllt sind.

    Returns:
        tuple: Aktualisierte Scatter-Punkte für die Animation.
    """
    # Berechne aktuelle Positionen der Teilchen
    x1_data = x1(t[frame])  # Position von Teilchen 1
    x2_data = x2(t[frame])  # Position von Teilchen 2

    # Setze die Positionen der Scatter-Punkte
    scatter1.set_offsets(np.array([[x1_data, 0]]))  # Teilchen 1 auf der X-Achse
    scatter2.set_offsets(np.array([[x2_data, 0.5]]))  # Teilchen 2 leicht versetzt auf der Y-Achse

    # Überprüfen der Resonanzbedingungen und Aktualisieren des Titels
    if resonance_condition(t[frame]):
        ax.set_title("Resonanz erreicht! Fusion möglich.", color="green")
    else:
        ax.set_title("Warten auf Resonanz...", color="red")

    # Rückgabe der aktualisierten Scatter-Punkte
    return scatter1, scatter2