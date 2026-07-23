# 🛠️ Poradnik Modyfikacji i Parametryzacji w OpenSCAD

Plik `scad/gimas_co2_holder.scad` zawiera w pełni parametryczny model 3D uchwytu na nabój CO2 do syfonów **GIMAS**. Dzięki budowie modułowej możesz łatwo dostosować wymiary, styl wykończenia, napisy tłoczone oraz rozszerzać projekt o własne warianty estetyczne.

---

## 🚀 Wymagane Oprogramowanie

- **OpenSCAD** w wersji 2021.01 lub nowszej (dostępny za darmo na [openscad.org](https://openscad.org/)).
- Opcjonalnie: Python 3 z pakietami `trimesh` i `pymeshlab` do automatycznego generowania i łączenia siatek w 100% szczelny wariant bryłowy (*watertight manifold*).

---

## ⚙️ Główne Parametry w Kodzie SCAD

Otwórz plik `scad/gimas_co2_holder.scad` w OpenSCAD. Na początku pliku znajdują się kluczowe zmienne:

```openscad
size = "12g"; // "8g" lub "12g"
style = 1;     // 1: Modern Minimalist, 2: Industrial Knurled, 3: Retro Fluted, 4: Ergonomic Spiral
$fn = 60;      // Gładkość zaokrągleń (zalecane 60 dla wysokiej jakości druku)
```

### 1. Zmiana Rozmiaru Naboju (`size`):
- `size = "8g"` – Uchwyt dostosowany do nabojów CO2 8g (całkowita długość 73 mm).
- `size = "12g"` – Uchwyt dostosowany do nabojów CO2 12g (całkowita długość 90 mm).

### 2. Wybór Stylu Wzorniczego (`style`):
- `style = 1` – **Modern Minimalist**: Gładki opływowy korpus z dwoma ergonomicznymi łopatkami.
- `style = 2` – **Industrial Knurled**: Pionowe żebra chwytne poprawiające chwyt mokrą dłonią.
- `style = 3` – **Retro Fluted**: Klasyczne wzdłużne żłobienia nawiązujące do syfonów vintage.
- `style = 4` – **Ergonomic Spiral**: Skręcona spiralnie powierzchnia wspomagająca naturalny ruch dokręcania.

---

## 💻 Kompilacja z Wiersza Poleceń (CLI)

Możesz wygenerować pliki STL bez otwierania interfejsu graficznego OpenSCAD:

```bash
# Wygenerowanie wersji 8g w stylu 1 (Modern):
openscad -D 'size="8g"' -D 'style=1' -o stl/gimas_co2_8g_styl1_modern.stl scad/gimas_co2_holder.scad

# Wygenerowanie wersji 12g w stylu 4 (Spiral):
openscad -D 'size="12g"' -D 'style=4' -o stl/gimas_co2_12g_styl4_spiral.stl scad/gimas_co2_holder.scad
```

---

## 🎨 Dostosowywanie Napisu Tłoczonego

W module `sleeve_shell()` znajduje się sekcja odpowiadająca za tłoczenie napisów:

```openscad
// Debossed vertical text
rotate([0, 0, 0]) translate([14.6, 0, len/2]) rotate([90, 0, 90]) rotate([0, 0, -90])
linear_extrude(height=5) text(text_str, size=8, font="Liberation Sans:style=Bold", halign="center", valign="center");
```

Możesz zmienić treść napisu (np. dodać własne inicjały lub markę), modyfikując argument `text_str` lub parametry czcionki (`size`, `font`).

---

## 🔄 Automatyzacja Budowania i Weryfikacji Siatek

W katalogu `scripts/` znajduje się skrypt w Pythonie:

```bash
python3 scripts/build_stl_and_renders.py
```

Skrypt automatycznie:
1. Kompiluje wszystkie warianty do modeli STL.
2. Wykonuje operację Boolean Union z fabrycznym gwintem M20.7, tworząc idealnie spójną bryłę (*manifold*).
3. Orientuje model w pionie (oś Z) z podstawą na Z=0.
4. Generuje podglądy PNG o rozdzielczości 1024x1024 w palecie *Sunset*.
