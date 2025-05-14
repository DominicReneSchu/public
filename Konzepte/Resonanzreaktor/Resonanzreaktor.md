# Resonanzreaktor – Konzept und Machbarkeit

Der **Resonanzreaktor** ist ein innovatives Energiekonzept, das auf supraleitenden Resonanzsystemen basiert. Ziel ist die effiziente Wandlung resonanter Energieimpulse in elektrische Energie – verlustarm, skalierbar und potenziell revolutionär.

---

## 1. Aufbau des Resonanzreaktors

| Komponente             | Funktion                                              | Technologische Basis                                 |
|------------------------|-------------------------------------------------------|------------------------------------------------------|
| **Resonanzkammer**     | Erzeugung resonanter Schwingungen                    | Supraleitende Kavitäten (z. B. Niob bei 4 K)         |
| **Magnetfeldführung**  | Frequenzsteuerung und Stabilisierung                 | Nb₃Sn-Magnete, HTS-Materialien                      |
| **Kryosystem**         | Kühlung auf < 4 K                                     | Helium-Kryostaten, Pulse-Tube-Cooler                |
| **Energieextraktion**  | Wandlung in elektrische Energie                       | Piezo- oder RF-Wandler, Photonenphononen-Kopplung   |
| **Steuerungseinheit**  | Echtzeitresonanzabgleich                              | FPGA-Systeme, adaptives Resonanztracking            |

---

## 2. Physikalische Grundlage

Die Energieumwandlung basiert auf einem resonanzverstärkten Impulsfluss, beschrieben durch:

$$\
P_{\text{net}} = \frac{P_{\text{res}}}{1 + \alpha(f, T)}
\$$

mit dem frequenz- und temperaturabhängigen Verlustfaktor:

$$\
\alpha(f, T) = \left( \frac{f^2}{T} \cdot e^{-\Delta / (k_B T)} + R_{\text{res}} \right) \cdot \frac{\sqrt{f}}{f_0 Q}
\$$

Dabei:
- $\ \Delta \$: Energielücke des Supraleiters (z. B. Niob: 1.5 meV)
- $\ R_{\text{res}} \$: Residualwiderstand
- $\ f_0 \$: Referenzfrequenz (z. B. 10 GHz)
- $\ Q \$: Gütefaktor (> 10⁸ möglich)
- $ T \$: Betriebstemperatur

---

## 3. Vergleich mit klassischen Reaktoren

| Kriterium              | Resonanzreaktor     | Fusionsreaktor (ITER) | Kernspaltung (AKW)  |
|------------------------|---------------------|------------------------|---------------------|
| **Energieträger**      | Resonanzschwingung  | Deuterium-Tritium      | Uran-235            |
| **Betriebstemperatur** | ~4 K                | 150 Mio. K             | ~600 K              |
| **Risiken**            | Magnetisch          | Neutronen, Plasma      | Meltdown, Abfall    |
| **Skalierbarkeit**     | Hoch                | Gering                 | Mittel              |

---

## 4. Simulation

Die Simulation in `Simulationen/Resonanzreaktor.py` berechnet die Nettoleistung bei Variation der Frequenz (1–100 GHz) und zeigt den Energiegewinn in Abhängigkeit der Materialparameter.

**Beispiel:**

```python
frequencies = np.linspace(1e9, 100e9, 1000)
P_net = P_res / (1 + loss_factor(frequencies, T))
´´´
