# Nichtlineare Resonanzanalyse – Interaktive Simulation

Dieses Tool visualisiert die Dynamik eines nichtlinearen, energie- und feldgekoppelten Oszillators auf Grundlage der **Resonanzfeldtheorie**. Die Simulation ist als interaktive Webanwendung umgesetzt (z. B. mit [Streamlit](https://streamlit.io)), und erlaubt die Live-Steuerung zentraler Systemparameter.

---

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

Über die Regler können zentrale Systemparameter wie Anregungsamplitude, Frequenz, Dämpfung und Simulationsdauer angepasst werden. So lässt sich das Systemverhalten in Echtzeit erforschen:

- **Amplitude (`Af`)** – Stärke der äußeren Anregung
- **Frequenz (`omega_f`)** – Frequenz der Anregung
- **Dämpfung (`d0`)** – Grunddämpfung des Systems
- **Federkonstante (`k`)** – Steifigkeit des Oszillators
- **Dauer (`T`)** – Simulationszeitraum

---

## Typische Parameter für maximale Energieübertragung

Um eine möglichst effektive Übertragung von Energie aus dem Resonanzfeld in mechanische Leistung zu erreichen, wähle folgende Parameterbereiche:

| Parameter     | Empfehlung                | Beschreibung |
|---------------|:------------------------:|:------------|
| **k**         | 1.0                      | Federkonstante |
| **m**         | 1.0                      | Masse |
| **omega_f**   | 1.0 – 1.05               | Anregungsfrequenz ≈ Eigenfrequenz (\(\omega_0 = \sqrt{k/m}\)) |
| **Af**        | 1.0 – 1.5                | Anregungsamplitude (nicht zu klein, nicht zu groß) |
| **d0**        | 0.05 – 0.1               | Unterkritische Dämpfung |
| **v0**        | 1.0                      | Normgeschwindigkeit für Rückkopplung |
| **beta**      | 0.05                     | Stärke der nichtlinearen Kopplung |
| **T**         | 100 – 200                | Simulationsdauer |
| **x0/v0 (init)** | 0.1 / 0.0             | Anfangsauslenkung/Geschwindigkeit |

**Hinweis:**  
Die beste Energieübertragung erreichst du, wenn die Anregungsfrequenz möglichst genau auf die Eigenfrequenz des Systems abgestimmt ist und die Dämpfung nicht zu stark ist. Zu hohe Amplituden oder zu starke Kopplung (\(\beta\)) führen häufig zu chaotischem Verhalten und weniger gezielter Energieübertragung.

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
3. Steuere die Parameter, starte die Simulation, und beobachte die Resultate live.

---

## Weiterführende Hinweise

- Die Simulation eignet sich zur Exploration klassischer und chaotischer Resonanzphänomene.
- Alle Visualisierungen sind direkt mit den Konzepten der Resonanzfeldtheorie verknüpft.
- Die App kann beliebig erweitert werden, z. B. um Lyapunov-Exponenten, Dimensionsschätzungen oder Batch-Parameter-Scans.
