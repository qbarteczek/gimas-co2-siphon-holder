# 🛠️ Bawimy się w OpenSCAD (Parametryzacja)

W folderze siedzi sobie plik `scad/gimas_co2_holder.scad` – to całe serce projektu. Jeśli chcesz wyczarować coś swojego na stary poczciwy syfon **GIMAS**, to dobrze trafiłeś. Kod jest podzielony tak, że bardzo łatwo cokolwiek zmienić.

---

## 🚀 Czego potrzebujesz?

- **OpenSCAD** w miarę świeży (od 2021.01). Darmowy, pobierzesz z [openscad.org](https://openscad.org/).
- Opcjonalnie: Python 3 z `trimesh` i `pymeshlab`, jeśli chcesz zautomatyzować generowanie pięknych, czystych siatek (watertight). 

---

## ⚙️ Co możemy pozmieniać w kodzie?

Na samej górze pliku `scad/gimas_co2_holder.scad` masz kilka parametrów. Wygląda to tak:

```openscad
size = "12g"; // Zmieniasz na "8g" jak wolisz mniejsze naboje
style = 1;     // Tu wybierasz swój ulubiony wzorek
$fn = 60;      // Rozdzielczość siatki (60 to już ładne koło)
```

### 1. Duży czy mały gaz? (`size`):
- `size = "8g"` – Klasyk, idealny pod małe naboje. Ma 73 mm.
- `size = "12g"` – Większa pojemność, 90 mm długości.

### 2. Wybieramy styl (`style`):
- `style = 1` – **Modern Minimalist**: Schludny, z dwoma płetwami ułatwiającymi wkręcanie.
- `style = 2` – **Industrial Knurled**: Radełko po całości. Fajna sprawa jak masz mokre ręce.
- `style = 3` – **Retro Fluted**: Takie klasyczne, szerokie rowki w stylu retro.
- `style = 4` – **Ergonomic Spiral**: Świderek. Wygląda cool i dobrze prowadzi dłoń przy kręceniu.

---

## 💻 Klepanie w konsoli

Jak nie lubisz wyklikiwać z interfejsu, to odpalasz to ładnie z terminala:

```bash
# Dla fana małych nabojów, wersja gładka (Modern):
openscad -D 'size="8g"' -D 'style=1' -o stl/gimas_co2_8g_styl1_modern.stl scad/gimas_co2_holder.scad

# Albo 12g świderek:
openscad -D 'size="12g"' -D 'style=4' -o stl/gimas_co2_12g_styl4_spiral.stl scad/gimas_co2_holder.scad
```

---

## 🎨 Własne napisy? Czemu nie!

Jeśli zajrzysz do modułu `sleeve_shell()`, znajdziesz tam kawałek kodu robiący wklęsły napis na boku:

```openscad
// Tu dzieje się magia wytłaczania tekstu
rotate([0, 0, 0]) translate([14.6, 0, len/2]) rotate([90, 0, 90]) rotate([0, 0, -90])
linear_extrude(height=5) text(text_str, size=8, font="Liberation Sans:style=Bold", halign="center", valign="center");
```

Możesz tu wpisać własne imię, nazwę babci, ksywkę, albo zmienić czcionkę. Eksperymentuj!

---

## 🔄 Wszystko na jednym kliknięciu (Python)

Nie chcesz się bawić z jednym plikiem? Wrzuciłem skrypt, który robi wszystko za Ciebie. Złoży, zszyje, zrenderuje:

```bash
python3 scripts/build_stl_and_renders.py
```

Co dokładnie robi ten skrypt?
1. Przelatuje przez wszystkie 4 style i 2 rozmiary.
2. Odpala MeshLaba w tle, żeby idealnie scalić nasz ładny korpus z gwintem M20.7, tworząc wzorowego STL-a bez błędów.
3. Stawia to równiutko w pionie (Z=0).
4. Strzela całkiem przyjemne podglądy PNG (z 3 stron!).
