# GIMAS Soda Siphon CO2 Cartridge Holder (8g & 12g)

[![OpenSCAD](https://img.shields.io/badge/OpenSCAD-Parametric-orange.svg)](https://openscad.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![3D Print Ready](https://img.shields.io/badge/3D%20Print-Watertight%20Manifold-brightgreen.svg)]()

Projekt monolitycznych, estetycznych uchwytów/nakładek na naboje CO2 (8g oraz 12g) do klasycznego syfonu do wody gazowanej marki **GIMAS**. 

Pliki STL stanowią w 100% zamkniętą, jednolitą bryłę (*Watertight Manifold Geometry*) z nagwintowanym otworem żeńskim **M20.7 x 2.0** idealnie pasującym do metalowej szyjki syfonu.

---

## 🎨 5 Wariantów Estetycznych (5 Unique Styles)

Kolekcja zawiera 5 unikalnych stylów wzorniczych opracowanych dla obu pojemności (8g oraz 12g):

| # | Nazwa Stylu | Opis | Cechy i Zalety | Plik STL (8g) | Plik STL (12g) |
|---|-------------|------|----------------|---------------|----------------|
| **1** | **Modern Minimalist** | Opływowy, gładki korpus z 2 łopatkami | Ergonomiczny chwyt, łatwy w czyszczeniu | `gimas_co2_8g_styl1_modern.stl` | `gimas_co2_12g_styl1_modern.stl` |
| **2** | **Industrial Knurled** | Radełkowane pionowe żebra chwytne | Surowy wygląd narzędziowy, pewny chwyt mokrą dłonią | `gimas_co2_8g_styl2_knurled.stl` | `gimas_co2_12g_styl2_knurled.stl` |
| **3** | **Tactical Hexagon** | Pancerny profil sześciokątny z fazowaniem | Sześciokątny przekrój z dodatkowymi skrzydełkami | `gimas_co2_8g_styl3_hexagon.stl` | `gimas_co2_12g_styl3_hexagon.stl` |
| **4** | **Retro Fluted** | Klasyczne wzdłużne żłobienia vintage | Stylistyka nawiązująca do syfonów z lat 70. | `gimas_co2_8g_styl4_fluted.stl` | `gimas_co2_8g_styl4_fluted.stl` |
| **5** | **Ergonomic Spiral** | Skręcone spiralnie żebra prowadzące | Naturalne dokręcanie zgodnie z ruchem dłoni | `gimas_co2_8g_styl5_spiral.stl` | `gimas_co2_12g_styl5_spiral.stl` |

---

## 🖨️ Zlecenia i Zalecane Parametry Druku 3D

> [!TIP]
> **Zalecenia dotyczące ustawień slicera (PrusaSlicer, Bambu Studio, Cura, OrcaSlicer):**
> - **Orientacja:** Dnem do dołu (gwint z góry, ułatwione chłodzenie otwarcia gwintowanego).
> - **Wysokość warstwy:** `0.20 mm` (lub `0.16 mm` dla wygładzonych gwintów).
> - **Liczba obrysów (Walls / Perimeters):** Minimum **4** (dla maksymalnej sztywności gwintu M20.7).
> - **Wypełnienie (Infill):** `20% - 30%` (Gyroid, Grid lub Rectilinear).
> - **Supporty (Wsporniki):** **BRAK** (kąty fazowania oraz wewnętrzny gwint i kopuła są zaprojektowane do druku bez podpór).
> - **Materiał:** **PETG**, **PLA** lub **ABS/ASA**. PETG zapewnia wysoką odporność mechaniczną przy wielokrotnym wkręcaniu.

---

## 🛠️ Budowanie i Parametryzacja w OpenSCAD

Kod źródłowy w `scad/gimas_co2_holder.scad` jest w pełni parametryczny.

### Generowanie z wiersza poleceń:
Możesz samodzielnie wygenerować dowolną kombinację używając OpenSCAD:

```bash
# Wygenerowanie wersji 8g w stylu Minimalist:
openscad -D 'size="8g"' -D 'style=1' -o stl/gimas_co2_8g_styl1_modern.stl scad/gimas_co2_holder.scad

# Wygenerowanie wersji 12g w stylu Knurled:
openscad -D 'size="12g"' -D 'style=2' -o stl/gimas_co2_12g_styl2_knurled.stl scad/gimas_co2_holder.scad
```

### Automatyczny skrypt budujący:
Projekt zawiera skrypt w Pythonie generujący pełną paczkę STL oraz renders:

```bash
python3 scripts/build_stl_and_renders.py
```

---

## 📐 Wymiary Techniczne

- **Gwint:** M20.7 x 2.0 (metryczny wewnętrzny profil syfonowy)
- **Komora zewnętrzna 8g:** Średnica 30.0 mm, długość całkowita 73 mm
- **Komora zewnętrzna 12g:** Średnica 30.0 mm, długość całkowita 90 mm
- **Komora wewnętrzna cartridża:** Średnica 19.2 mm
- **Zwieńczenie:** Gładka zaokrąglona kopuła dociskająca nabój do iglicy syfonu.

---

## 📜 Licencja

Ten projekt dostępny jest na licencji [MIT](LICENSE).
