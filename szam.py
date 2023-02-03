import random


def veletlen_szam():
    vel = int((random.random()*50)+1)
    return vel


def oszthato(vel):

    if vel % 5 == 0 and vel % 3 == 0:
        eredmeny = f" A szám öttel és hárommal is osztható!"
    elif vel % 3 == 0:
        eredmeny = f" A szám hárommal osztható!"
    elif vel % 5 == 0:
        eredmeny = f" A szám öttel osztható!"
    else:
        eredmeny = f" Nem osztható sem 3-al sem 5-el!"

    return eredmeny
