# Memóriajáték Python

## Hallgató
**Név:** Varga Ádám
**Neptun-kód:** H3CBR8

## Feladat leírása
Ez a projekt egy egyszerű memóriajátékot valósít meg Pythonban, a **Tkinter** grafikus felület könyvtár segítségével.  
A játék célja, hogy a felhasználó minden pár kártyát megtaláljon a lehető legkevesebb lépésből és időből.  
A játék végén a pontszám a megtett lépések és az eltelt idő alapján kerül kiszámításra, a legjobb eredmények pedig egy **Top lista** ablakban jelennek meg.

## Szükséges modulok
- Python 3.x
- tkinter (grafikus felület)
- random (beépített)
- time (beépített)
- os (beépített)

## Modulok és a modulokban használt függvények

### 1. `main.py`
- Fő modul, amely a játék felületét és logikáját kezeli.
- **Osztály:** `MemoriaJatekVA`
- **Főbb függvények/metódusok:**
  - `__init__(self, master)`: Inicializálja a játékot, betölti a képeket, létrehozza a gombokat.
  - `letrehoz_tabla_va(self)`: Létrehozza a játéktábla gombjait.
  - `kattintas_va(self, index)`: Kezeli a kártyákra történő kattintásokat.
  - `ellenoriz_par_va(self)`: Ellenőrzi, hogy a két felfedett kártya megegyezik-e.
  - `vege_va(self)`: A játék végén kiszámítja és menti a pontszámot, majd megjeleníti a toplistát.
  - `uj_jatek_va(self)`: Új játékot indít, visszaállítja a játéktáblát és a változókat.
  - `mutat_toplista_va(self, vegso_pont=None, lepesek=None, ido=None)`: Megjeleníti a Top listát, opcionálisan az utolsó játék eredményével.
  - `megnyit_sugo_va(self)`: Megnyitja a súgó ablakot a játékszabályokkal.

### 2. `utils_va.py`
- Segédfüggvényeket tartalmaz a pontszámítás és a Top lista kezeléséhez.
- **Függvények:**
  - `pontszam_szamitas_va(lepesek, ido)`: Kiszámítja a pontszámot a lépések és az eltelt idő alapján.
  - `mentes_pontszam_va(pont, ido, lepesek, fajlnev="highscore.txt")`: Ment egy új pontszámot a fájlba.
  - `beolvas_pontszamok_va(fajlnev="highscore.txt")`: Beolvassa a mentett pontszámokat, és visszaadja listaként.

## Osztály

### `MemoriaJatekVA` (main.py)
- Kezeli a játék logikáját és a felhasználói felületet.
- **Attribútumok:**
  - `self.master`: A Tkinter főablak.
  - `self.kivalasztott`: Az aktuálisan kiválasztott kártyák indexei.
  - `self.felfedett`: A már párosított kártyák indexei.
  - `self.lepesek`: Az eddigi lépések száma.
  - `self.start_ido`: A játék kezdete.
  - `self.kepmappa`: A képek könyvtára.
  - `self.hatlap`: A kártya hátlap képe.
  - `self.kepfajlok`: A kártyaképek listája.
  - `self.kepek`: Betöltött képek listája.
  - `self.kartya_lista`: A játékban használt kártyák képei duplikálva és összekeverve.
  - `self.gombok`: A Tkinter gombok listája.
- **Metódusok:** lásd a "Modulok és a modulokban használt függvények" résznél.

---

**Megjegyzés:** A játék a `kepek` mappában tárolt képeket használja, amelynek tartalmaznia kell a `hatlap.png` és a játékhoz szükséges képeket (pl. `cica.png`, `kutya.png`, `alma.png`, stb.).
