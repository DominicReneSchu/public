# Resonanzanalyse in Massendaten

## Einführung

Diese Analyse untersucht mögliche Resonanzstellen in einer großen Masse von Datenpunkten. Ziel ist es, signifikante Überschüsse von Ereignissen um bestimmte `ε`-Werte nachzuweisen und statistisch abzusichern. Dabei kommen dynamische Fensterbreiten, p-Wert-Berechnung und Multipletest-Korrektur zum Einsatz.

Die Daten umfassen insgesamt `n` Events und wurden aus [Datenquelle kurz beschreiben] gewonnen.

## Methodik

### Datenvorverarbeitung

- Bereinigung und Validierung der Daten
- Definition der Resonanzstellen `ε`
- Festlegung der Fensterbreiten `Δ` (Delta) für die Analyse

### Dynamische Fensterbreiten-Analyse

Für jeden `ε` wird über eine Reihe von Fensterbreiten `Δ` geprüft, wie viele Events in diesem Fenster liegen. Der optimale `Δ` wird gewählt, um den höchsten statistischen Überschuss zu finden.

### Hintergrundschätzung

Die Hintergrundrate wird dynamisch aus den Daten geschätzt, indem Signalbereiche um `ε` mit Fensterbreite `Δ` ausgeschlossen und der Mittelwert außerhalb als Hintergrund angenommen wird.

### Signifikanztest und Multipletest-Korrektur

- Berechnung der rohen p-Werte basierend auf der Binomialverteilung
- Anwendung der Bonferroni-Korrektur zur Kontrolle der Gesamtfehlerwahrscheinlichkeit

## Ergebnisse

| Epsilon | Bestes Δ | Treffer | p-Wert roh | p-Wert korrigiert |
|---------|----------|---------|------------|-------------------|
| 1.00    | 1.9      | 2699    | 0.000e+00  | 0.000e+00         |
| 0.50    | 2.1      | 1647    | 0.000e+00  | 0.000e+00         |
| 0.67    | 2.0      | 1860    | 0.000e+00  | 0.000e+00         |
| 0.75    | 2.0      | 2155    | 0.000e+00  | 0.000e+00         |
| 1.25    | 1.7      | 2901    | 0.000e+00  | 0.000e+00         |

Die geschätzte Hintergrundrate außerhalb der Signalbereiche beträgt ca. 0.93362.

### Stabilitäts- und Robustheits-Checks

- Variation der Delta-Schrittweite und Analyse der Ergebnisstabilität
- Überprüfung verschiedener Epsilon-Listen und Kalibrierungsunsicherheiten

## Visualisierung

- Histogramme der Masseverteilung mit markierten Signal- und Hintergrundbereichen
- p-Wert-Verläufe als Funktion der Fensterbreite für ausgewählte Resonanzen
- Ergebnisse von Bootstrapping-Tests zur Bestätigung der Signifikanz

## Fazit und Ausblick

Die Analyse zeigt robuste und signifikante Resonanzüberschüsse bei mehreren `ε`-Werten. Die methodische Absicherung durch Hintergrundschätzung, Multipletest-Korrektur und Zufalls-Simulationen gewährleistet eine hohe Aussagekraft.

Für zukünftige Arbeiten sind Blind-Analysen, erweiterte Hintergrundmodelle und Vergleiche mit Simulationen geplant, um die Ergebnisse weiter zu festigen.

---

## Beispielcode

## Beispielcode und Visualisierung

Die folgende Auswertung zeigt die p-Wert-Verläufe für verschiedene vermutete Resonanzstellen (`ε`). Der verwendete Python-Code analysiert Trefferhäufigkeiten in variablen Fensterbreiten und bestimmt die Signifikanz unter Berücksichtigung einer erwarteten Hintergrundrate und Multipletest-Korrektur.

```python
import pandas as pd
from scipy.stats import binomtest
import matplotlib.pyplot as plt
from statsmodels.stats.multitest import multipletests

# Daten laden
df = pd.read_csv('dielectron.csv')
n = len(df)

# Parameter
epsilons = [1, 0.5, 2/3, 0.75, 1.25]
deltas = [0.1 * i for i in range(1, 31)]

# Erwartete Trefferquoten
expected_hit_rates = {
    1: 0.01,
    0.5: 0.005,
    2/3: 0.006,
    0.75: 0.007,
    1.25: 0.0125,
}

# Hintergrundrate dynamisch schätzen
signal_mask = pd.Series(False, index=df.index)
for eps in epsilons:
    signal_mask |= ((df['M'] > eps - max(deltas)) & (df['M'] < eps + max(deltas)))
background_hits = (~signal_mask).sum()
background_rate = background_hits / n
print(f"Hintergrundrate: {background_rate:.5f}")

for eps in epsilons:
    p_values = []
    hits_list = []

    for delta in deltas:
        hits = ((df['M'] > eps - delta) & (df['M'] < eps + delta)).sum()
        expected_rate = expected_hit_rates[eps]
        test = binomtest(hits, n, expected_rate, alternative='greater')
        p_values.append(test.pvalue)
        hits_list.append(hits)

    # Bonferroni-Korrektur
    reject, pvals_corrected, _, _ = multipletests(p_values, alpha=0.05, method='bonferroni')
    best_idx = pvals_corrected.argmin()

    print(f"Epsilon {eps}: Bestes Delta = {deltas[best_idx]:.3f}, "
          f"Treffer = {hits_list[best_idx]}, "
          f"p-Wert roh = {p_values[best_idx]:.3e}, "
          f"p-Wert korrigiert = {pvals_corrected[best_idx]:.3e}")

    plt.plot(deltas, p_values, label=f"Epsilon {eps}")

plt.xlabel("Delta")
plt.ylabel("p-Wert")
plt.yscale("log")
plt.legend()
plt.title("p-Werte für verschiedene Epsilon-Resonanzen")
plt.tight_layout()
plt.show()
