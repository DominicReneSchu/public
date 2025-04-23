## Vergleich: Konventionelle Drehmomentberechnung vs. ResoCalc (Resonanzfeldtheorie)

In diesem Abschnitt vergleichen wir die klassische mechanische Berechnung des effektiven Drehmoments mit der neuen Methode auf Basis der **Resonanzfeldtheorie** (ResoCalc).

👉 **Direkt zur Anwendung:**  
[![⚡ ResoCalc starten](https://img.shields.io/badge/⚡_ResoCalc_starten-Resonanzfeld_theorie-orange)](https://resoshift.com/)

### Ausgangswerte:
- Masse: $$m = 2\,\mathrm{kg}$$  
- Länge: $$l = 1\,\mathrm{m}$$  
- Anregungsfrequenz: $$f = 10\,\mathrm{Hz}$$  
- Resonanzfrequenz: $$f_r = 5\,\mathrm{Hz}$$  
- Kopplungsfaktor: $$\zeta = 0{,}2$$

---

### Berechnungsansätze:

#### 🔵 Konventionell (klassisch):  
Effektives Drehmoment:

\[
M_{\text{konv}} = J \cdot \omega^2 \cdot \frac{\theta_{\text{max}}}{\sqrt{2}} \quad \text{mit} \quad J = m \cdot l^2
\]

Dabei ist $$\theta_{\text{max}}$$ eine willkürlich gewählte Auslenkung – ein fundamentaler Schwachpunkt des klassischen Ansatzes.

---

#### 🔴 ResoCalc (Resonanzfeldtheorie – wie im Code verwendet):

\[
M_{\text{reso}} = I \cdot (2\pi f)^2 \cdot \frac{1}{\sqrt{(1 - (f / f_r)^2)^2 + (2 \zeta \cdot (f / f_r))^2}}
\]

mit:
- $$I = m \cdot l^2$$: Trägheitsmoment
- $$\zeta$$: Kopplungsfaktor (bzw. $$\zeta = \frac{1}{Q}$$ bei Gütefaktor-Eingabe)

---

### Ergebnis:
| Methode       | Effektives Drehmoment |
|---------------|------------------------|
| Konventionell | 558,3 Nm              |
| ResoCalc      | 2543,0 Nm             |

> ⚠️ Die frühere symbolische Formel mit Betrag und 0.5-Faktor war eine vereinfachte Näherung und wurde **nicht in der ResoCalc-Implementierung verwendet**.

---

### Visualisierung:

![Vergleich: ResoCalc vs. Konventionell](resocalcVSkonv.png)

---

### Fazit:
**ResoCalc ersetzt den klassischen Rechenweg durch eine realitätsnahe, resonanzbasierte Verstärkungsformel – ganz ohne Annahmen über die Auslenkung.**  
Die Ergebnisse sind stabil, reproduzierbar und direkt technisch nutzbar – auch im Grenzbereich der Resonanz.
