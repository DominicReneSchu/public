# Monte-Carlo-Simulation zur Resonanzanalyse

## Einleitung

Die Monte-Carlo-Simulation ist ein zentrales Werkzeug in der statistischen Auswertung wissenschaftlicher Datensätze. In dieser Analyse dient sie dazu, die Wahrscheinlichkeit zu bestimmen, mit der ein beobachteter Überschuss an Ereignissen im Bereich einer vermuteten Resonanzstelle (**ε**) rein zufällig durch den Hintergrund erklärt werden könnte.

## Ziel

Das Ziel ist es, die empirische Signifikanz (p-Wert) der Beobachtungen zu quantifizieren, indem viele Hintergrund-Szenarien simuliert und mit den realen Daten verglichen werden.

## Methodik

### Hintergrundmodellierung

* Die Hintergrundverteilung wird aus den Messdaten extrahiert – unter explizitem Ausschluss der Signalbereiche (um die untersuchten **ε**).
* Ein Kernel-Density-Estimator (KDE) wird verwendet, um daraus eine glatte Wahrscheinlichkeitsverteilung zu erzeugen.

### Durchführung der Monte-Carlo-Simulation

* Es werden viele (z.B. 1.000–10.000) *Pseudo-Experimente* durchgeführt, bei denen jeweils die gleiche Anzahl an Events wie im Originaldatensatz aus dem KDE-Modell gezogen wird.
* Für jedes *Pseudo-Experiment* wird die vollständige Resonanzanalyse wiederholt:

  * Trefferzahlen in variablen Fenstern (**Δ**) um jedes **ε** werden bestimmt.
  * Die p-Werte werden mit den gleichen Tests wie für die Originaldaten berechnet.
  * Die jeweils optimalen Fenstergrößen werden automatisch bestimmt.
* Es werden die jeweils extremsten Trefferzahlen und p-Werte dokumentiert.

### Bestimmung des empirischen p-Werts

* Der empirische p-Wert ist der Anteil der Simulationsdurchläufe, in denen ein ebenso extremer oder extremerer Überschuss wie in den realen Daten gefunden wurde.
* Beispiel: Ist der empirische p-Wert ≈ 0, wurde in keiner Simulation ein so starkes Signal wie in den echten Daten beobachtet.

## Visualisierung der Ergebnisse

### 1. Monte-Carlo-Hits vs. echte Treffer

Das Histogramm zeigt, wie häufig in der Monte-Carlo-Simulation bestimmte Trefferzahlen im optimalen Fenster für jedes **ε** vorkommen. Die rote Linie markiert den Wert aus den echten Daten.

![Histogramm MC vs Echt](report_out/figures/hist_mc_vs_real_hits.png)

---

### 2. p-Wert-Verläufe über die Fensterbreite **Δ**

Hier siehst du für jede Resonanzstelle **ε** die p-Werte aus den MC-Simulationen (Median und 68%-Intervall) und den realen Daten in Abhängigkeit von **Δ**.

![p-Wert-Verläufe](report_out/figures/pvalue_curves.png)

---

### 3. Heatmaps: Trefferanzahl über **ε** und **Δ**

Die Heatmaps zeigen die Trefferzahlen für alle Kombinationen aus **ε** und **Δ**, einmal für die realen Daten und einmal als Mittelwert der Monte-Carlo-Simulationen.

![Heatmaps Trefferanzahl](report_out/figures/heatmaps_hits.png)

---

## Interpretation

* Die Monte-Carlo-Simulation zeigt, wie außergewöhnlich die beobachteten Überschüsse im Vergleich zum Hintergrund sind.
* Empirische p-Werte < 0,01 – insbesondere p ≈ 0 – sprechen für eine extrem geringe Wahrscheinlichkeit, dass die Befunde durch Zufall entstehen.
* Die grafische Gegenüberstellung (Histogramme, p-Wert-Kurven, Heatmaps) macht die Differenz zwischen Signal und Hintergrund anschaulich.

## Hinweise zum Code

* Die Simulation nutzt `scikit-learn` für KDE, `numpy` und `pandas` für Datenhandling und `matplotlib` für die Visualisierung.
* Fortschrittsbalken (`tqdm`) zeigen den Simulationsfortschritt an.
* Alle wichtigen Parameter wie **ε**, **Δ** und die Anzahl der Simulationen sind zentral in `config.py` eingestellt.
* Die wichtigsten Plots werden automatisch im Ordner `report_out/figures` abgelegt und sind hier direkt eingebunden.

## Fazit

Die Monte-Carlo-Methode bietet eine robuste Möglichkeit zur statistischen Validierung von Resonanzeffekten. Durch die gezielte Modellierung des Hintergrunds und die wiederholte Zufallssimulation liefert sie eine belastbare Grundlage für die Signifikanzabschätzung.

Zukünftige Erweiterungen könnten adaptive Fenstergrößen, multiple Hypothesentests oder Bayesianische Ansätze integrieren.

---

⬅️ [zurück](../../../README.md)



---

⬅️ [zurück](../../../README.md)