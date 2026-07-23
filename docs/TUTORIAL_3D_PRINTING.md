# 🖨️ Jak to wydrukować? (Poradnik Druku 3D)

Krótka piłka: ten uchwyt musi wytrzymać trochę siły, jak dokręcasz gaz do syfonu **GIMAS**. Dlatego gwint M20.7 to najważniejszy punkt zabawy. Niżej zebrałem ustawienia, które sprawdzą się u każdego.

---

## 📐 Slicer – o czym pamiętać

| Ustawienie | Co dać | Po co to? |
|:---|:---|:---|
| **Jak położyć na stole** | **Dnem na blachę** (gwint do góry) | Żeby łatwo schłodzić gwint i uniknąć nawisów, które mogłyby wszystko zepsuć. |
| **Wysokość warstwy** | `0.16 mm` lub `0.20 mm` | Przy `0.16 mm` gwint wyjdzie po prostu masełko. |
| **Obrysy (Walls)** | **4 do 5 sztuk** | **Najważniejsze!** Nie żałuj obrysów. Gwint musi być twardy jak skała, a z małą ilością ścianek wypełnienie tylko osłabi sprawę. |
| **Góra/Dół (Top/Bottom)** | **5 warstw z góry i dołu** | Czapeczka na górze musi znieść ciśnienie dociskanego naboju. |
| **Wypełnienie** | `25% - 30%` | Daj Gyroid (żyroid) – fajnie znosi siły z każdej strony. |
| **Podpory (Supports)** | **Wyłącz (Off)** | Szkoda czasu, model tak zaprojektowałem, że puści bez żadnych rusztowań. |

---

## 🧵 Z czego drukujemy?

1. **PETG (Zdecydowanie polecam):**
   - **Plusy:** Plastik, który wybacza dużo, ładnie się klei i nie pęknie ci gwint, jak będziesz go mocno dokręcać co weekend.
   - **Temperatury:** Zależy od szpuli, ale celuj w `230-240°C` i stół na `70-80°C`.

2. **ASA / ABS:**
   - **Plusy:** Pancerne, do tego jak ktoś lubi, to wygładzi oparami z acetonu i wyjdzie "jak z fabryki".
   - **Minusy:** Musisz uważać na skurcz. Jak ci podwinie, gwint nie wejdzie. Lepiej drukować w komorze.

3. **PLA (Jak nie masz nic innego):**
   - **Plusy:** Drukuje się samo, jest bardzo twarde.
   - **Minusy:** Daj to pod gorącą wodę i popłynie. Żadnych zmywarek! 

---

## 💡 Składanie i drobne patenty

1. **Pierwsze podejście z gwintem:**
   - Wiadomo, plastikowy gwint potrzebuje chwili, żeby dogadać się z metalem w syfonie. Wkręcaj z czuciem, jeśli idzie ciężko, wkręć trochę i wykręć – taki "tapping" na szybko.
2. **Dodaj trochę poślizgu:**
   - Możesz kropnąć odrobinę smaru silikonowego (spożywczego) na gwint. Później wkręca się jednym palcem.
3. **Zapinamy pasy:**
   - Jak wrzucisz nabój i zakręcasz uchwyt, zrób to płynnym, zdecydowanym ruchem na samym końcu. Usłyszysz syk, dociśnij do końca i gotowe!

---

## ❓ FAQ – co może pójść nie tak?

- **Q: Kurde, gwint wchodzi megaciężko, co robić?**
  - *A:* Odpal w slicerze opcję `Slicing Tolerance` i rzuć na `Exclusive` (lub zmień `XY Size Compensation` o np. `-0.05 mm`). Trochę to zluzuje szczeliny.
- **Q: Góra mi nie pęknie jak docisnę nabój?**
  - *A:* Spokojna głowa! Dałem tam ze 4 milimetry pełnego plastiku. Przy 5 obrysach można po tym niemalże skakać, iglicę przebije na luzie.
