import tkinter as tk
from tkinter import PhotoImage, Toplevel
import random
import time
import os
from utils_va import pontszam_szamitas_va, mentes_pontszam_va, beolvas_pontszamok_va

class MemoriaJatekVA:
    def __init__(self, master):
        self.master = master
        self.master.title("Memóriajáték")

        self.kivalasztott = []
        self.felfedett = []
        self.lepesek = 0
        self.start_ido = time.time()

        self.kepmappa = "kepek"
        self.hatlap = PhotoImage(file=os.path.join(self.kepmappa, "hatlap.png"))
        self.kepfajlok = ["cica.png", "kutya.png", "alma.png", "banan.png", "auto.png", "hajo.png"]
        self.kepek = [PhotoImage(file=os.path.join(self.kepmappa, f)) for f in self.kepfajlok]

        self.kartya_lista = self.kepek * 2
        random.shuffle(self.kartya_lista)
        self.gombok = []
        self.letrehoz_tabla_va()

        self.uj_jatek_gomb = tk.Button(
            self.master, text="Új játék", width=12, height=2, font=("Arial", 12),
            command=self.uj_jatek_va
        )
        self.toplista_gomb = tk.Button(
            self.master, text="Top lista", width=12, height=2, font=("Arial", 12),
            command=self.mutat_toplista_va
        )
        self.kilepes_gomb = tk.Button(
            self.master, text="Kilépés", width=12, height=2, font=("Arial", 12),
            command=self.master.quit
        )
        self.sugo_gomb = tk.Button(
            self.master, text="Súgó", width=12, height=2, font=("Arial", 12),
            command=self.megnyit_sugo_va
        )

        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

        self.uj_jatek_gomb.grid(row=4, column=0, sticky="ew", padx=5, pady=10)
        self.toplista_gomb.grid(row=4, column=1, sticky="ew", padx=5, pady=10)
        self.sugo_gomb.grid(row=4, column=2, sticky="ew", padx=5, pady=10)
        self.kilepes_gomb.grid(row=4, column=3, sticky="ew", padx=5, pady=10)

    def letrehoz_tabla_va(self):
        for index, kep in enumerate(self.kartya_lista):
            gomb = tk.Button(self.master, image=self.hatlap,
                             command=lambda idx=index: self.kattintas_va(idx))
            gomb.grid(row=index//4, column=index%4, padx=5, pady=5)
            self.gombok.append(gomb)

    def kattintas_va(self, index):
        if index in self.felfedett or index in self.kivalasztott:
            return

        if len(self.kivalasztott) >= 2:
            return

        self.gombok[index].config(image=self.kartya_lista[index])
        self.kivalasztott.append(index)

        if len(self.kivalasztott) == 2:
            self.lepesek += 1
            self.master.after(1000, self.ellenoriz_par_va)

    def ellenoriz_par_va(self):
        i1, i2 = self.kivalasztott
        if self.kartya_lista[i1] == self.kartya_lista[i2]:
            self.felfedett.extend([i1, i2])
        else:
            self.gombok[i1].config(image=self.hatlap)
            self.gombok[i2].config(image=self.hatlap)
        self.kivalasztott = []

        if len(self.felfedett) == len(self.kartya_lista):
            self.vege_va()

    def vege_va(self):
        ido = time.time() - self.start_ido
        pont = pontszam_szamitas_va(self.lepesek, ido)
        mentes_pontszam_va(pont, ido, self.lepesek)
        self.mutat_toplista_va(vegso_pont=pont, lepesek=self.lepesek, ido=int(ido))

    def uj_jatek_va(self):
        for gomb in self.gombok:
            gomb.destroy()
        self.gombok.clear()
        self.kivalasztott = []
        self.felfedett = []
        self.lepesek = 0
        self.start_ido = time.time()
        self.kartya_lista = self.kepek * 2
        random.shuffle(self.kartya_lista)
        self.letrehoz_tabla_va()

    def mutat_toplista_va(self, vegso_pont=None, lepesek=None, ido=None):
        eredmenyek = beolvas_pontszamok_va()
        top = sorted(eredmenyek, key=lambda x: int(x[0]), reverse=True)[:5]

        ablak = tk.Toplevel(self.master)
        ablak.title("Top lista")
        szoveg = ""
        if vegso_pont is not None:
            szoveg += f"Játék vége!\nPontszám: {vegso_pont}, Lépések: {lepesek}, Idő: {ido} mp\n\n"

        szoveg += "Top eredmények:\n"
        for sor in top:
            szoveg += f"{sor[0]} pont - {sor[1]} mp - {sor[2]} lépés\n"

        label = tk.Label(ablak, text=szoveg, font=("Arial", 11), justify="left")
        label.pack(padx=10, pady=10)

    def megnyit_sugo_va(self):
        ablak = tk.Toplevel(self.master)
        ablak.title("Súgó")
        szoveg = (
            "Memóriajáték súgó:\n\n"
            "- Kattints két kártyára, hogy felfedd őket.\n"
            "- Ha a két kártya megegyezik, megmaradnak felfedve, ha nem akkor visszafordulnak.\n"
            "- A cél: minden párt megtalálni a lehető legkevesebb lépésből és időből.\n"
            "- A pontszám a lépések és az idő alapján kerül kiszámításra.\n"
            "- Top lista highscore.txt-ben tárolodik az első játéktól kezdve.\n"
        )
        label = tk.Label(ablak, text=szoveg, font=("Arial", 11), justify="left")
        label.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoriaJatekVA(root)
    root.mainloop()
