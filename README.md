# 🍾 GIMAS Soda Siphon CO2 Cartridge Holder (8g & 12g)

[![OpenSCAD](https://img.shields.io/badge/OpenSCAD-Parametric-orange.svg)](https://openscad.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![3D Print Ready](https://img.shields.io/badge/3D%20Print-Watertight%20Manifold-brightgreen.svg)]()

Projekt monolitycznych, estetycznych uchwytów/nakładek na naboje CO2 (8g oraz 12g) do klasycznego syfonu do wody gazowanej marki **GIMAS**.

Pliki STL stanowią w 100% zamkniętą, jednolitą bryłę (*Watertight Manifold Geometry*) z nagwintowanym otworem żeńskim **M20.7 x 2.0** idealnie pasującym do metalowej szyjki syfonu oraz półokrągłą kopułą dociskową.

---

## 🎨 4 Warianty Estetyczne (4 Unique Styles)

Kolekcja zawiera 4 dopracowane warianty stylistyczne opracowane dla obu pojemności (8g oraz 12g):

| # | Podgląd | Nazwa Stylu | Opis | Cechy i Zalety | Plik STL (8g) | Plik STL (12g) |
|---|:---:|-------------|------|----------------|---------------|----------------|
| **1** | <img src="renders/gimas_co2_12g_styl1_modern.png" width="120"> | **Modern Minimalist** | Opływowy, gładki korpus z 2 łopatkami | Ergonomiczny chwyt, łatwy w czyszczeniu | [`8g Modern`](stl/gimas_co2_8g_styl1_modern.stl) | [`12g Modern`](stl/gimas_co2_12g_styl1_modern.stl) |
| **2** | <img src="renders/gimas_co2_12g_styl2_knurled.png" width="120"> | **Industrial Knurled** | Radełkowane pionowe żebra chwytne | Surowy wygląd narzędziowy, pewny chwyt mokrą dłonią | [`8g Knurled`](stl/gimas_co2_8g_styl2_knurled.stl) | [`12g Knurled`](stl/gimas_co2_12g_styl2_knurled.stl) |
| **3** | <img src="renders/gimas_co2_12g_styl3_fluted.png" width="120"> | **Retro Fluted** | Klasyczne wzdłużne żłobienia vintage | Stylistyka nawiązująca do syfonów z lat 70. | [`8g Fluted`](stl/gimas_co2_8g_styl3_fluted.stl) | [`12g Fluted`](stl/gimas_co2_12g_styl3_fluted.stl) |
| **4** | <img src="renders/gimas_co2_12g_styl4_spiral.png" width="120"> | **Ergonomic Spiral** | Skręcone spiralnie żebra prowadzące | Naturalne dokręcanie zgodnie z ruchem dłoni | [`8g Spiral`](stl/gimas_co2_8g_styl4_spiral.stl) | [`12g Spiral`](stl/gimas_co2_12g_styl4_spiral.stl) |

---

## 📚 Poradniki i Dokumentacja (Guides & Tutorials)

W katalogu [`docs/`](docs/) znajdują się szczegółowe poradniki i instrukcje:

1. 🖨️ **[Poradnik Druku 3D (3D Printing Tutorial)](docs/TUTORIAL_3D_PRINTING.md)**
   - Ustawienia slicera (PrusaSlicer, Bambu Studio, OrcaSlicer, Cura).
   - Dobór filamentu (PETG, ASA, PLA) i wytrzymałość gwintu M20.7.
   - Orientacja druku bez użycia podpór (*no supports*).

2. 🛠️ **[Poradnik Modyfikacji OpenSCAD (Customization Guide)](docs/TUTORIAL_OPENSCAD_CUSTOMIZATION.md)**
   - Parametryzacja modelu w `scad/gimas_co2_holder.scad`.
   - Zmiana czcionki i wytłaczanych napisów.
   - Kompilacja z wiersza poleceń (CLI) i automatyzacja w Pythonie.

3. 🍾 **[Instrukcja Obsługi Syfonu GIMAS (Siphon Usage Guide)](docs/SIPHON_USAGE_GUIDE.md)**
   - Krok po kroku: napełnianie, wkręcanie, nasycanie gazem CO2 i serwowanie.
   - Bezpieczeństwo i zalecenia eksploatacyjne.

---

## 🖨️ Szybkie Zalecenia Druku 3D

> [!TIP]
> **Skrócone parametry druku:**
> - **Orientacja:** Dnem do dołu (gwint z góry, ułatwione chłodzenie otwarcia gwintowanego).
> - **Wysokość warstwy:** `0.16 mm` lub `0.20 mm`.
> - **Liczba obrysów (Walls / Perimeters):** Minimum **4 - 5** (dla pełnej sztywności gwintu M20.7).
> - **Wypełnienie (Infill):** `25% - 30%` (Gyroid lub 3D Honeycomb).
> - **Supporty (Wsporniki):** **BRAK** (kąty fazowania oraz wewnętrzny gwint i kopuła są zaprojektowane do druku bez podpór).
> - **Materiał:** **PETG** (rekomendowany) lub **ASA/ABS**.

---

## 🛠️ Budowanie i Parametryzacja w OpenSCAD

Kod źródłowy w [`scad/gimas_co2_holder.scad`](scad/gimas_co2_holder.scad) jest w pełni parametryczny.

### Generowanie z wiersza poleceń:
```bash
# Wygenerowanie wersji 8g w stylu Minimalist:
openscad -D 'size="8g"' -D 'style=1' -o stl/gimas_co2_8g_styl1_modern.stl scad/gimas_co2_holder.scad

# Wygenerowanie wersji 12g w stylu Knurled:
openscad -D 'size="12g"' -D 'style=2' -o stl/gimas_co2_12g_styl2_knurled.stl scad/gimas_co2_holder.scad
```

### Automatyczny skrypt budujący:
```bash
python3 scripts/build_stl_and_renders.py
```

---

## 📐 Wymiary Techniczne

- **Gwint:** M20.7 x 2.0 (metryczny wewnętrzny profil syfonowy)
- **Długość całkowita 8g:** 73.0 mm (średnica zewnętrzna 30.0 mm)
- **Długość całkowita 12g:** 90.0 mm (średnica zewnętrzna 30.0 mm)
- **Zwieńczenie:** Gładka zaokrąglona kopuła dociskająca nabój do iglicy syfonu.

---

## 📜 Licencja

Ten projekt dostępny jest na licencji [MIT](LICENSE).
