import numpy as np

# Funktionen zur Berechnung der Positionen der Teilchen
def x1(t):
    """
    Berechnet die Position von Teilchen 1 basierend auf einer sinusförmigen Bewegung.
    
    Args:
        t (float or numpy.ndarray): Zeitpunkte für die Berechnung der Position.
        
    Returns:
        numpy.ndarray: Position(en) von Teilchen 1.
    """
    return np.sin(t)

def x2(t):
    """
    Berechnet die Position von Teilchen 2 basierend auf einer kosinusförmigen Bewegung.
    
    Args:
        t (float or numpy.ndarray): Zeitpunkte für die Berechnung der Position.
        
    Returns:
        numpy.ndarray: Position(en) von Teilchen 2.
    """
    return np.cos(t)