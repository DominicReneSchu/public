# Simulation einer Wandstruktur: Ein Leitfaden

In dieser Simulation haben wir ein einfaches, zweidimensionales Kraftfeld erstellt, das eine Wandstruktur darstellt. Die Wandstruktur wird durch die Wechselwirkungen von Resonanzfrequenzen in einem dynamischen Feld modelliert. In dieser Simulation verwenden wir die **Schu-Gleichung**, die auf den grundlegenden Naturkonstanten basiert, um die Energieverteilung zu berechnen.

## 1. Die mathematischen Grundlagen

Die mathematische Grundlage dieser Simulation basiert auf der **Schu-Gleichung**, die die Energie $$\ E(x, y) \$$ in einem zweidimensionalen Raum beschreibt:

$$
E(x, y) = \sigma(x, y) \cdot \pi \cdot h \cdot f(x, y)
\$$

- $$\ \sigma(x, y) \$$ ist die Kopplungsdichte des Feldes, die angibt, wie stark das Feld an einer bestimmten Position ist.
- $$\ \pi \$$ ist die Kreiszahl (Schu-Kompass), die als Maß für Resonanzkreise dient.
- $$\ h \$$ ist das Plancksche Wirkungsquantum, das als Maß für die Quantisierung der Energie dient.
- $$\ f(x, y) \$$ beschreibt das Resonanzfrequenzfeld, das hier durch stehende Wellen modelliert wird.

## 2. Die Simulation

Die Simulation verwendet ein zweidimensionales Gitter, um die Resonanzfrequenz und Kopplungsdichte zu berechnen. In diesem Fall haben wir eine Wandstruktur erzeugt, indem die Kopplungsdichte in einem Bereich stark erhöht und außerhalb dieses Bereichs abgeschwächt wurde.

### 2.1. Der Code

Hier ist der vollständige Python-Code, der die Simulation umsetzt:

```python
import numpy as np
import matplotlib.pyplot as plt

# Konstanten
pi = np.pi                         # Kreiszahl Pi (Schu-Kompass)
h = 6.626e-34                      # Plancksches Wirkungsquantum in J·s

# Raumgitter definieren (x, y im Bereich -1 bis 1)
x = np.linspace(-1, 1, 400)
y = np.linspace(-1, 1, 400)
X, Y = np.meshgrid(x, y)

# Resonanzfrequenzfeld f(x, y): stehende Wellenform
f = np.sin(10 * pi * X) * np.sin(10 * pi * Y)

# Wand-ähnliche Struktur (Kopplung sehr stark in der Mitte, schwächer am Rand)
sigma = np.exp(-10 * (X**2 + Y**2))  # zentrale starke Kopplung
sigma[(X > -0.2) & (X < 0.2) & (Y > -1.0) & (Y < 1.0)] = 10  # starke Wand im Bereich

# Schu-Gleichung: E(x, y) = σ · π · h · f
E = sigma * pi * h * f

# Visualisierung der Energieverteilung
plt.figure(figsize=(6, 5))
plt.contourf(X, Y, E, levels=100, cmap='viridis')
plt.colorbar(label='Energieverteilung E(x, y)')
plt.title('Simulation einer Wandstruktur')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(False)
plt.tight_layout()
plt.show()
   ```
---

© Dominic-René Schu – Resonanzfeldtheorie 2025

1. **Repository klonen**:  
   ```bash
   git clone https://github.com/DominicReneSchu/public.git
   cd Resonanzfeldtheorie
   ```

---

⬅️ [Zurück zur Startseite](../../README.md)