import streamlit as st
import numpy as np

# Titel der App
st.title("Optimierte Resonanz-Brennstab Berechnung")

# Eingabewerte
f_ziel = st.number_input("Ziel-Frequenz [Hz]", value=160.0)  # Ziel-Frequenz 160 Hz
m = st.number_input("Masse [kg]", value=0.01, format="%.4f")  # 0.01 kg
L = st.number_input("Länge [m]", value=0.05, format="%.4f")  # 0.05 m
r = st.number_input("Radius [m]", value=0.01, format="%.4f")  # 0.01 m
D = st.number_input("Drehsteifigkeit D [Nm]", value=1e-9, format="%.2e")  # 1e-9 Nm

# Konstanten
h_ev = 4.135667696e-15  # Planck-Konstante [eV·s]

# Trägheitsmoment eines Vollzylinders um seine Achse
I = 0.5 * m * r**2  # [kg·m²]

# Polares Flächenträgheitsmoment
J = 0.5 * np.pi * r**4  # [m⁴]

# Berechnung der erforderlichen Energie, um die Ziel-Frequenz zu erreichen
def berechne_energie(f_ziel, I, D):
    return (2 * np.pi * I * f_ziel)**2 * I / D  # Umgekehrte Berechnung der Energie [Joules]

# Berechnung der benötigten Energie
E_joule = berechne_energie(f_ziel, I, D)

# Ausgabe der berechneten Werte
st.markdown(f"**Benötigte Energie, um {f_ziel} Hz zu erreichen:** {E_joule:.2e} Joules")
st.markdown(f"**Trägheitsmoment I:** {I:.2e} kg·m²")
st.markdown(f"**Polares Flächenträgheitsmoment J:** {J:.2e} m⁴")
st.markdown(f"**Drehsteifigkeit D:** {D:.2e} Nm")
