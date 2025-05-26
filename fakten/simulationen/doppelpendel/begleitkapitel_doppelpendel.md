# Begleitkapitel: Interaktive Simulation des Doppelpendels

Dieses Kapitel erläutert die Hintergründe, Funktionsweise und Umsetzung der interaktiven Doppelpendel-Simulation, wie sie im vorliegenden Python-Code realisiert ist. Ziel der Anwendung ist es, die dynamischen Eigenschaften eines Doppelpendels anschaulich und intuitiv erfahrbar zu machen.

---

## 1. Physikalische Grundlagen

Das Doppelpendel ist ein klassisches Beispiel für ein nichtlineares, chaotisches System. Es besteht aus zwei starren Pendelarmen, die über ein Scharnier miteinander verbunden sind. Die Bewegungsgleichungen ergeben sich aus der Lagrange-Mechanik und sind in einschlägiger Standardliteratur (z. B. Goldstein, "Classical Mechanics") ausführlich hergeleitet. Sie erfassen die Zeitentwicklung der Winkelpositionen und Winkelgeschwindigkeiten beider Pendel.

Die Differentialgleichungen sind gekoppelt und nichtlinear, sodass sie i. d. R. numerisch mit Methoden wie Runge-Kutta (hier: `scipy.integrate.solve_ivp`) gelöst werden.

---

## 2. Interaktive Steuerung

Über die im Interface implementierten **Slider** können die wichtigsten Systemparameter unmittelbar verändert werden:

- **Startwinkel** (`θ₁`, `θ₂`): Anfangsauslenkungen beider Pendelarme
- **Anfangswinkelgeschwindigkeiten** (`ω₁`, `ω₂`): Startwerte für die Drehgeschwindigkeiten
- **Massen** (`m₁`, `m₂`): Massen der beiden Pendelarme
- **Längen** (`L₁`, `L₂`): Längen der Pendelarme

Jede Veränderung eines Sliders setzt die Simulation mit den neuen Werten zurück und startet die Animation neu, sodass die Auswirkungen der Parameteränderungen direkt beobachtet werden können.

---

## 3. Animation und Trail

Die Animation zeigt die Bewegung des Doppelpendels im Zeitverlauf. Zusätzlich werden die **Spuren (Trails)** der beiden Massenpunkte als farbige Linien eingeblendet. Diese Trails visualisieren den Bewegungsverlauf der beiden Massen über die letzten *N* Frames (konfigurierbar über `TRAIL_LENGTH`). Dadurch werden typische chaotische Bahnmuster des Doppelpendels sichtbar.

---

## 4. Kapselung und Zustandshandling

Die gesamte Pendeldynamik und der aktuelle Zustand des Systems sind in einer eigenen **Klasse** (`DoublePendulumSim`) gekapselt. Diese Klasse verwaltet die aktuellen Parameter, berechnet die Bewegungsgleichungen und speichert die numerisch integrierte Lösung. Die Kapselung ermöglicht eine saubere Trennung zwischen Modelldaten und Darstellungs-/Interaktionslogik.

---

## 5. Technische Umsetzung (Kurzüberblick)

- **Numerische Lösung:** `scipy.integrate.solve_ivp` (Runge-Kutta-Verfahren)
- **Visualisierung:** `matplotlib` (Animation, Slider-Widgets)
- **Benutzerinteraktion:** Slider für alle relevanten Start- und Systemparameter
- **Animation:** `FuncAnimation` (Kontinuierliche Aktualisierung und Darstellung der Simulation)
- **Trail-Logik:** Speicher der letzten `TRAIL_LENGTH` Positionen für die Spurendarstellung

---

## 6. Erweiterungsmöglichkeiten

Mögliche Erweiterungen der Simulation umfassen:
- Energieskala/Diagramm (Gesamtenergie im Zeitverlauf)
- Export von Trajektorien
- Zusätzliche Dämpfungsterms oder Reibung
- Dreidimensionale Darstellung

---

## 7. Fazit

Die entwickelte Simulation verbindet anschauliche Visualisierung, Interaktivität und numerische Physik. Sie ist ein effektives Werkzeug, um die komplexen Bewegungen und das chaotische Verhalten des Doppelpendels explorativ zu erleben und zu verstehen.

---

*© Dominic Schu, 2025 – Alle Rechte vorbehalten.*

---

⬅️ [zurück](../README.md)