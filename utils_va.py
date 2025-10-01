def pontszam_szamitas_va(lepesek, ido):
    return max(1000 - (lepesek * 10 + int(ido)), 0)

def mentes_pontszam_va(pont, ido, lepesek, fajlnev="highscore.txt"):
    with open(fajlnev, "a", encoding="utf-8") as f:
        f.write(f"{pont};{int(ido)};{lepesek}\n")

def beolvas_pontszamok_va(fajlnev="highscore.txt"):
    try:
        with open(fajlnev, "r", encoding="utf-8") as f:
            return [sor.strip().split(";") for sor in f.readlines()]
    except FileNotFoundError:
        return []
