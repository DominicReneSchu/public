import numpy as np

def update(frame, scatter1, scatter2, ax, t, x1, x2, resonance_condition):
    # Berechne die Positionen der Teilchen im aktuellen Frame
    x1_data = x1(t[frame])  # Position von Teilchen 1
    x2_data = x2(t[frame])  # Position von Teilchen 2

    # Setze die Position der Scatter-Punkte für die Teilchen im aktuellen Frame
    scatter1.set_offsets(np.array([[x1_data, 0]]))  # Teilchen 1 auf der X-Achse
    scatter2.set_offsets(np.array([[x2_data, 0.5]]))  # Teilchen 2 leicht versetzt auf der Y-Achse

    # Überprüfen, ob Resonanz auftritt und den Titel ändern
    if resonance_condition(t[frame]):
        ax.set_title("Resonanz erreicht! Fusion möglich.", color="green")
    else:
        ax.set_title("Warten auf Resonanz...", color="red")
    
    return scatter1, scatter2
