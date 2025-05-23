# Nichtlineare Resonanzanalyse – Interaktive Simulation

## Was zeigt die Simulation?

### 1. Zeitverlauf der Auslenkung `x(t)`
Der Plot oben links zeigt die Bewegung des Oszillators über die Zeit. Je nach gewählter Anregung und Dämpfung kann das Verhalten periodisch, quasiperiodisch oder chaotisch sein.

### 2. Phasenraumdiagramm `(x, v)`
Hier sieht man, wie sich die Systemzustände im Phasenraum (Auslenkung vs. Geschwindigkeit) entwickeln. Geschlossene Bahnen deuten auf periodische Bewegung, komplexe Muster auf chaotische Dynamik und Resonanzvernetzung hin.

### 3. Poincaré-Schnitt `(x, v)` bei Anregungsphase = 0
Der Poincaré-Schnitt ist ein klassisches Werkzeug aus der nichtlinearen Dynamik. Er zeigt nur die Systemzustände, wenn die Phase der äußeren Anregung ein ganzzahliges Vielfaches von \(2\pi\) erreicht. Dadurch werden wiederkehrende Muster und Resonanzinseln sichtbar – ein zentrales Merkmal komplexer Resonanzfelder.

### 4. Frequenzspektrum (Fourier)
Hier wird gezeigt, welche Frequenzen in der Bewegung dominieren. Periodische Systeme zeigen einen Hauptpeak, chaotische Systeme ein breites Spektrum.

### 5. Spektrogramm (Zeit-Frequenz-Analyse)
Das Spektrogramm (Kurzzeit-Fourier-Transformation) visualisiert, wie sich die Frequenzanteile im Verlauf der Zeit verändern. Damit lassen sich Übergänge zwischen geordneten und chaotischen Phasen erkennen.

### 6. Wavelet-Skalogramm (optional)
Das Wavelet-Skalogramm zeigt die Zeit-Frequenz-Struktur mit besonders guter Auflösung für nichtstationäre oder kurzzeitige Resonanzphänomene (z. B. plötzliche chaotische Einbrüche).

---

## Interaktive Parametersteuerung

Über die Regler können zentrale Systemparameter angepasst werden. So lässt sich das Systemverhalten in Echtzeit erforschen:

- **Af** – Anregungsamplitude (Stärke der äußeren Anregung)
- **omega_f** – Anregungsfrequenz (Frequenz der äußeren Anregung)
- **T** – Simulationsdauer
- **d0** – Dämpfungsfaktor (Grunddämpfung des Systems)
- **k** – Federkonstante (Steifigkeit des Oszillators)
- **v0** – Normgeschwindigkeit für Skalen der Rückkopplung

---

## Typische Parameter für maximale Energieübertragung

Um eine möglichst effektive Übertragung von Energie aus dem Resonanzfeld in mechanische Leistung zu erreichen, wähle folgende Parameterbereiche:

| Parameter   | Empfehlung         | Beschreibung |
|-------------|:-----------------:|:-------------|
| **Af**      | 1.0 – 1.5         | Nicht zu klein, damit genügend Energie eingespeist wird |
| **omega_f** | 1.0 – 1.05        | Möglichst nahe an der Eigenfrequenz (\(\omega_0 = \sqrt{k}\) bei \(m=1\)) |
| **d0**      | 0.05 – 0.1        | Unterkritische Dämpfung (nicht zu stark) |
| **k**       | 1.0               | Standardwert für die Federkonstante |
| **v0**      | 1.0               | Typischer Wert für Normgeschwindigkeit |
| **T**       | 100 – 200         | Simulationszeitraum, ausreichend lang für Resonanzeffekte |

**Hinweis:**  
Die beste Energieübertragung erreichst du, wenn die Anregungsfrequenz möglichst genau auf die Eigenfrequenz des Systems abgestimmt ist und die Dämpfung nicht zu stark ist. Zu hohe Amplituden führen ggf. zu chaotischem Verhalten und weniger gezielter Energieübertragung.

**Typische Anzeichen für effektive Energieaufnahme:**  
- Große, regelmäßige Auslenkungen im Zeitplot.
- Hauptpeak im Frequenzspektrum bei der Anregungsfrequenz.
- Klare, strukturierte Resonanzinseln im Poincaré-Schnitt.

---

## Theoretischer Hintergrund

Das Modell basiert auf der **Resonanzfeldtheorie**. Hier werden System und Umgebung nicht getrennt betrachtet, sondern als miteinander rückgekoppeltes Resonanzfeld. Die beobachteten Muster (Resonanzinseln, Chaos, Fraktale) sind direkte Ausprägungen dieser Feldstruktur.

### Typische Phänomene:

- **Resonanzinseln**: Gebiete im Poincaré-Schnitt, in denen das System bevorzugt verweilt – Ausdruck stabiler Resonanzmoden.
- **Chaos & Fraktalität**: Unvorhersagbare, komplexe Muster, die auf eine dichte Vernetzung der Resonanzmoden hinweisen.
- **Ordnungs-Chaos-Übergänge**: Im Spektrogramm/Wavelet sichtbar als zeitlich begrenzte Bereiche mit veränderten Frequenzmustern.

---

## Nutzung

1. Installiere die benötigten Pakete:
   ```
   pip install streamlit numpy matplotlib scipy pywt
   ```
2. Starte die App:
   ```
   streamlit run app.py
   ```
3. Steuere die Parameter, starte die Simulation und beobachte die Resultate live.

---

## Weiterführende Hinweise

- Die Simulation eignet sich zur Exploration klassischer und chaotischer Resonanzphänomene.
- Alle Visualisierungen sind direkt mit den Konzepten der Resonanzfeldtheorie verknüpft.
- Die App kann beliebig erweitert werden, z. B. um Lyapunov-Exponenten, Dimensionsschätzungen oder Batch-Parameter-Scans.