# Simulationsergebnisse: Resonanzreaktor

Diese Datei dokumentiert die Ergebnisse der Simulation eines Resonanzreaktors mit Plutonium-239 als Ausgangsmaterial. Die Simulation untersucht das Verhalten des Materials über mehrere Zeitschritte, einschließlich Anregungsniveau und Transmutation.

---

## Simulationsparameter

- **Ausgangsmaterial**: Plutonium-239
- **Neutronenfluss**: 1e13 Teilchen/cm²/s
- **Temperatur**: 350 Kelvin
- **Anzahl der Zeitschritte**: 10
- **Dauer eines Zeitschritts**: 1 Jahr

---

## Ergebnisse

### Tabelle der Ergebnisse

| Zeitschritt | Material         | Anregungsniveau (Excitation Level) |
|-------------|------------------|------------------------------------|
| 1           | Plutonium-239    | 0.85                               |
| 2           | Plutonium-239    | 0.73                               |
| 3           | Plutonium-239    | 0.62                               |
| 4           | Plutonium-239    | 0.52                               |
| 5           | Americium-241    | 0.45                               |
| 6           | Americium-241    | 0.39                               |
| 7           | Americium-241    | 0.33                               |
| 8           | Americium-241    | 0.28                               |
| 9           | Americium-241    | 0.24                               |
| 10          | Americium-241    | 0.20                               |

---

### Interpretation der Ergebnisse

1. **Materialwechsel**:
   - Die Simulation zeigt, dass Plutonium-239 ab dem 5. Zeitschritt in Americium-241 transmutiert wurde. Dies ist das Ergebnis des hohen Neutronenflusses, der die Transmutation gemäß den physikalischen Modellen auslöste.

2. **Anregungsniveau (Excitation Level)**:
   - Das Anregungsniveau nimmt mit der Zeit ab. Dies ist auf die Zerfallsprozesse des Materials und die abnehmende Resonanzanregung zurückzuführen.
   - Nach der Transmutation zu Americium-241 bleibt das Anregungsniveau niedriger, da Americium-241 eine geringere Resonanzfrequenz und Energie pro Zerfall aufweist.

3. **Einfluss von Temperatur und Neutronenfluss**:
   - Die Temperatur beeinflusst die Resonanzfrequenz, was sich auf die Anregungsniveaus auswirkt.
   - Der hohe Neutronenfluss war entscheidend für die Transmutation von Plutonium-239 zu Americium-241.

---

## Grafische Darstellung

Die Ergebnisse der Simulation wurden zusätzlich grafisch dargestellt. Die Diagramme umfassen:

1. **Exzitationslevel des Materials**:
   - Ein Liniendiagramm zeigt die Abnahme des Anregungsniveaus über die Zeitschritte.

2. **Materialtransmutation**:
   - Ein Stufendiagramm zeigt den Wechsel des Materials von Plutonium-239 zu Americium-241.

---

## Schlussfolgerungen

- **Effizienz der Transmutation**:
  - Die Simulation bestätigt, dass ein hoher Neutronenfluss effektiv zur Transmutation langlebiger Isotope wie Plutonium-239 beiträgt.

- **Zukünftige Untersuchungen**:
  - Weitere Simulationen mit unterschiedlichen Materialien, Temperaturen und Neutronenflüssen könnten zusätzliche Erkenntnisse über die Dynamik des Resonanzreaktors liefern.

---

_Ende der Simulationsergebnisse_

# Simulation des Zerfalls und der Transmutation von Isotopen

## Übersicht

Die Simulation modelliert den Zerfall und die Transmutation von Isotopen über eine gegebene Zeitspanne. Sie berücksichtigt dabei die physikalischen Eigenschaften der Isotope, wie Halbwertszeit, Resonanzfrequenz, freigesetzte Energie und mögliche Transmutationspfade.

---

## Hauptkomponenten der Simulation

### 1. **Isotopenklasse**
- **Eigenschaften**:
  - **Halbwertszeit**: Zeit, nach der die Hälfte des Isotops zerfallen ist.
  - **Resonanzfrequenz**: Charakteristische Frequenz des Isotops.
  - **Zerfallskonstante**: Maß für die Zerfallsrate.
  - **Energie pro Zerfall**: Energiemenge (in MeV), die bei jedem Zerfall freigesetzt wird.
  - **Transmutationen**: Liste von Isotopen, in die das aktuelle Isotop übergehen kann.

---

### 2. **Zerfallsmethode**
- Berechnet den verbleibenden Anteil des Isotops nach einer gegebenen Zeitspanne.
- Verwendet die exponentielle Zerfallsgleichung:  
  
  $$\
  N(t) = N_0 \cdot e^{-\lambda \cdot t}
  \$$  
  wobei $$\ \lambda\$$ die Zerfallskonstante ist.

---

### 3. **Energiefreisetzung**
- Die freigesetzte Energie wird basierend auf der Anzahl der Zerfälle und der Energie pro Zerfall berechnet:
  
  $$\
  E(t) = N(t) \cdot \text{Energie pro Zerfall}
  \$$

---

### 4. **Transmutation**
- Wenn ein Isotop eine Transmutation zu einem anderen Isotop durchläuft, wird das neue Isotop zurückgegeben.
- Transmutationen sind in einer Kette definiert, die das Verhalten des Isotops über die Zeit beschreibt.

---

### 5. **Simulation**
- **Funktion**: `simulate_decay_chain(isotope, time_span)`
- **Beschreibung**: Simuliert den Zerfall und die Transmutation eines Isotops über eine bestimmte Zeitspanne.
- **Eingaben**:
  - `isotope`: Das Ausgangsisotop.
  - `time_span`: Die Zeitspanne der Simulation in Jahren.
- **Ausgaben**:
  - Jährliche Anzeige des verbleibenden Isotops und der freigesetzten Energie.
  - Hinweis auf Transmutationen, wenn das Isotop in ein anderes übergeht.

---

## Beispiel: Zerfallskette von Uranium-235

### Ausgangsbedingungen:
- **Startisotop**: Uranium-235
- **Zeitspanne**: 10 Jahre

### Ergebnis:
- Uranium-235 durchläuft die Transmutation zu Plutonium-239 und schließlich zu Americium-241.
- Für jedes Jahr wird die Energie berechnet und angezeigt, bis die Kette keine weiteren Transmutationen mehr hat.

### Simulationscode:
```python
simulate_decay_chain(uranium_235, 10)
```

### Beispielausgabe:
```
Jahr 0: Uranium-235 mit 200.00 MeV freigegebener Energie
Transmutation zu Plutonium-239 erfolgt.
Jahr 1: Plutonium-239 mit 180.00 MeV freigegebener Energie
Transmutation zu Americium-241 erfolgt.
Jahr 2: Americium-241 mit 5.50 MeV freigegebener Energie
Kein weiterer Zerfall oder Transmutation für Americium-241.
Endgültiges Isotop: Americium-241
```

---

## Anpassungen und Erweiterungen

- **Andere Isotope**: Für andere Isotope kann die Simulation durch Anpassung der Eingabeparameter erweitert werden.
- **Komplexere Ketten**: Die Transmutationskette kann erweitert werden, um zusätzliche Schritte zu berücksichtigen.
- **Visualisierung**: Eine grafische Darstellung der freigesetzten Energie und der Materialzusammensetzung über die Zeit könnte hinzugefügt werden.

---

## Fazit

Die Simulation bietet eine flexible Möglichkeit, den Zerfall und die Transmutation von Isotopen zu modellieren. Sie kann für verschiedene Anwendungen in der Kernphysik, Reaktordesign und Nuklearwissenschaft genutzt werden.