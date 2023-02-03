kor = []

def bekert_szam():
    a = 0
    i = 0
    while i < 5:
        korok = int(input(f"\t Kérlek adj meg egy számot melyek egy személy korának felel meg!"))
        kor.append(korok)
        i += 1
    while a < len(kor)-1:
        print(kor[a], end=":")
        a += 1
    print(kor[a])


def elso_idos():
    idos = 0
    i = 0
    while i < len(kor):
        if kor[i] >= 70 and idos == 0:
            idos = i+1
        i += 1
    return idos


def beolvasas(idos):
    fajlom = open("oreg.txt", "w", encoding="UTF-8")
    fajlom.write(f"Az első idős ember korának helye a listába:{idos}")
    fajlom.close()








