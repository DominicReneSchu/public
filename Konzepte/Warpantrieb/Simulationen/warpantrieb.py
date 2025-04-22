import streamlit as st
import numpy as np

st.title("Resonanz-Brennstab Optimierung")

# Eingaben
f_ziel = st.slider("Ziel-Frequenz [Hz]", 10, 1000, 160)
r = st.slider("Radius [cm]", 1, 10, 2) / 100  # Umrechnung in Meter
rho = st.slider("Materialdichte [kg/m³]", 5000, 25000, 19000)

# Konstanten
E = 1e-3           # Eingebrachte Energie [eV]
D = 1e-22          # Drehsteifigkeit [Nm]
eV_to_J = 1.602e-19
E_J = E * eV_to_J  # Umrechnung in Joule

# Funktionen
def schu_frequenz(E, I, D):
    return (E / (2 * np.pi * I)) * np.sqrt(D / I)

def optimales_I(E, D, f):
    return ((E * np.sqrt(D)) / (2 * np.pi * f))**(2/3)

# Berechnung
I_opt = optimales_I(E_J, D, f_ziel)
m = I_opt / (0.5 * r**2)
V = m / rho
h = V / (np.pi * r**2)
f_berechnet = schu_frequenz(E_J, I_opt, D)

# Ausgabe
st.write(f"**Optimales Trägheitsmoment:** {I_opt:.2e} kg·m²")
st.write(f"**Benötigte Masse:** {m:.3f} kg")
st.write(f"**Zylinderlänge:** {h:.3f} m")
st.write(f"**Berechnete Frequenz:** {f_berechnet:.2f} Hz")
