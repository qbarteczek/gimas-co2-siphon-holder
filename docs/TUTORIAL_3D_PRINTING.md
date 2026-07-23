# 🖨️ Poradnik Druku 3D – Uchwyty CO2 GIMAS (8g & 12g)

Ten dokument zawiera optymalne parametry druku 3D dla wariantów uchwytów CO2 do syfonów **GIMAS**. Przestrzeganie poniższych zaleceń gwarantuje wysoką wytrzymałość mechaniczną gwintu M20.7 oraz stuprocentową szczelność i trwałość pod naciskiem iglicy syfonu.

---

## 📐 Rekomendowane Ustawienia w Slicera (PrusaSlicer / Bambu Studio / OrcaSlicer / Cura)

| Parametr | Rekomendowana Wartość | Uwagi / Opis |
|:---|:---|:---|
| **Orientacja na stole** | **Dnem do dołu** (gwintem w górę) | Ułatwia chłodzenie otwarcia gwintowanego, eliminując zwisy. |
| **Wysokość warstwy (Layer Height)** | `0.16 mm` lub `0.20 mm` | Dla precyzyjnego i gładkiego gwintu M20.7 polecamy warstwę `0.16 mm`. |
| **Liczba obrysów (Perimeters / Walls)** | **4 do 5** | **Kluczowa cecha!** Zapewnia pełny profil gwintu ze ścianek obrysu bez osłabiającego wypełnienia. |
| **Górne i dolne warstwy (Top/Bottom Layers)** | **5 górnych, 5 dolnych** | Zapewnia szczelne i odporne na nacisk zamknięcie kopuły dociskowej. |
| **Wypełnienie (Infill Density)** | `25% - 30%` | Pattern **Gyroid** lub **3D Honeycomb** (świetne rozłożenie sił osiowych). |
| **Podpory (Support Structure)** | **BRAK (Off)** | Wszystkie warianty zaprojektowano z kątami fazowania pozwalającymi na druk bez podpór. |
| **Szerokość linii (Line Width)** | `0.40 mm` do `0.45 mm` (przy dyszy 0.4 mm) | Dobre scalenie warstw. |

---

## 🧵 Wybór Materiału (Filamentu)

1. **PETG (Zalecany / Best Choice):**
   - **Zalety:** Wysoka odporność uderzeniowa i elastyczność, świetna adhezja warstw, odporność na wilgoć oraz brak kruszenia się gwintu przy częstym wkręcaniu.
   - **Temperatura:** Dysza `230-240°C`, stół `70-80°C`.

2. **ASA / ABS:**
   - **Zalety:** Wyjątkowa twardość, możliwość wygładzania oparami acetonu (dla idealnego połysku).
   - **Uwagi:** Wymaga zamkniętej komory drukowania, aby uniknąć skurczu przy gwincie.

3. **PLA (Dopuszczalny do zastosowań domowych):**
   - **Zalety:** Bardzo łatwy w druku, wysoka sztywność.
   - **Uwagi:** Może ulec odkształceniu pod wpływem wysokiej temperatury (np. w zmywarce lub gorącej wodzie). Nie myć w zmywarkach!

---

## 💡 Wskazówki Montażowe i Wykończeniowe

1. **Pierwsze wkręcenie:**
   - Gwint M20.7 w modelu został zaprojektowany z odpowiednią tolerancją fabryczną. Pierwsze wkręcenie na metalową szyjkę syfonu GIMAS powinno odbyć się płynnie. Jeśli czujesz opór, wykonaj ruch wkręcająco-wykręcający (jak przy gwintowaniu).
2. **Smarowanie gwintu (Opcjonalnie):**
   - Nałożenie minimalnej ilości smaru silikonowego bezpiecznego dla żywności lub wazeliny technicznej ułatwia wkręcanie i zabezpiecza gwint przed zużyciem.
3. **Dokręcanie z nabojem CO2:**
   - Przy dokręcaniu uchwytu z włożonym nabojem CO2 dokręcaj zdecydowanym, płynnym ruchem do momentu przebicia błony naboju przez iglicę syfonu.

---

## ❓ FAQ – Często Zadawane Pytania

- **Q: Gwint wkręca się zbyt ciasno, co zrobić?**
  - *A:* Sprawdź w slicerze ustawienie `Slicing Tolerance` (ustaw na `Middle` lub `Exclusive`) albo skoryguj `XY Size Compensation` / `Internal Hole Clearance` o `-0.05 mm`.
- **Q: Czy górna kopuła wytrzyma nacisk naboju?**
  - *A:* Tak! Kopuła ma grubość ponad 4 mm i przy minimum 5 warstwach top oraz 4 obrysach przenosi obciążenia osiowe znacznie przekraczające siłę potrzebną do przebicia iglicy.
