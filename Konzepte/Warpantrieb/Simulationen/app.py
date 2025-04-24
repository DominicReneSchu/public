import streamlit as st
import numpy as np
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
st.title("Schu-Frequenzrechner")

E = 1e-3
D = 1e-22
rho = 19000
r = 0.02

f_ziel = st.slider("Ziel-Frequenz [Hz]", 10, 1000, 160)

def schu_frequenz(E, I, D):
    return (E / (2 * np.pi * I)) * np.sqrt(D / I)

def optimales_I(E, D, f):
    return ((E * np.sqrt(D)) / (2 * np.pi * f))**(2/3)

I_opt = optimales_I(E, D, f_ziel)
m = I_opt / (0.5 * r**2)
V = m / rho
h = V / (np.pi * r**2)

f_schu = schu_frequenz(E, I_opt, D)

st.write(f"**Optimales Trägheitsmoment:** {I_opt:.2e} kg·m²")
st.write(f"**Zylinderlänge bei 2cm Radius:** {h:.3f} m")
st.write(f"**Masse:** {m:.3f} kg")
st.write(f"**Berechnete Frequenz:** {f_schu:.2f} Hz")
