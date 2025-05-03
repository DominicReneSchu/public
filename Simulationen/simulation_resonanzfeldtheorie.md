# Resonanzfeld-Simulation mit Schu-Gleichung

Diese interaktive Simulation visualisiert die Energieübertragung zwischen zwei schwingenden Oszillatoren basierend auf der **Schu-Gleichung**:

$$\
E = \pi \cdot \varepsilon \cdot h \cdot (f_1 + f_2)
\$$

Dabei sind:
- $$\ f_1, f_2 \$$: Eigenfrequenzen der Oszillatoren  
- $$\ \varepsilon \$$: Kopplungsstärke  
- $$\ h \$$: Plancksches Wirkungsquantum oder alternativ eine neue Naturkonstante \( \eta \)  
- $$\ \pi \$$: Kreiszahl im Sinne des Schu-Kompasses  

## Features

- Auswahl der Kopplungsart:
  - **Linear**: $$\ E_\mathrm{trans} = \varepsilon \cdot \psi_1 \cdot \psi_2 \$$
  - **Quadratisch**: $$\ E_\mathrm{trans} = \varepsilon \cdot \psi_1^2 \cdot \psi_2 \$$
  - **Trigonometrisch**: $$\ E_\mathrm{trans} = \varepsilon \cdot \sin(\psi_1) \cdot \sin(\psi_2) \$$
- Anzeige der **Resonanzbedingung** basierend auf rationalem Frequenzverhältnis \( f_1 / f_2 = n / m \$$
- Optionale Verwendung einer neuen Naturkonstante \( \eta \) statt \( h \$$
- Interaktive Visualisierung über `ipywidgets`

## Voraussetzungen

- Python ≥ 3.8  
- Jupyter Notebook / JupyterLab  
- Installierte Pakete:

```bash
pip install numpy matplotlib ipywidgets
```

## Simulation

➡️ [Simulation](https://github.com/DominicReneSchu/public/tree/main/Simulationen)
➡️ [Zurück zum Hauptprojekt](../README.md)
