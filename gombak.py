from Gomba import Gomba

nev = []
nemzettseg = []
evszak = []

def beolvas():
    f = open("gombak_jav.txt", "r", encoding="UTF-8")
    fejlec = f.readline()
    sorok = f.readlines()
    f.close()
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split('@')
        nev.append(sor[0])
        nemzettseg.append(sor[1])
        evszak.append(sor[2])
        i += 1


def gombak_szama():
    x = len(nev)
    return x


def papsapka():
    i = 0
    while i < len(nev) and nemzettseg[i] != 'papsapkagombák ':
        i += 1
    return nev[i]


def tinoru():
    tin_szam = 0
    i = 0
    while i < len(nemzettseg):
        if nemzettseg[i] == "tinóru":
            tin_szam += 1
        i += 1
    return tin_szam
