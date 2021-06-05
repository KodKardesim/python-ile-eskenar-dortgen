def sagSlas(adet):
    for i in range(int(adet)):
        print("/", end="")


def solSlas(adet):
    for i in range(int(adet)):
        print("\\", end="")


def satirAtla(adet):
    for i in range(int(adet)):
        print()


def bosluk(adet):
    for i in range(int(adet)):
        print(" ", end="")


def ust(cap):
    basbosluk = (cap / 2) - 1
    for i in range(int(cap / 2)):
        bosluk(basbosluk - i)
        sagSlas(1)
        bosluk(i * 2)
        solSlas(1)
        satirAtla(1)


def alt(cap):
    basbosluk = cap - 2
    for i in range(int(cap / 2)):
        bosluk(i)
        solSlas(1)
        bosluk(basbosluk - (i * 2))
        sagSlas(1)
        satirAtla(1)


def ucgen(cap):
    ust(cap)
    alt(cap)


ucgen(int(input("Çap giriniz (çift sayı) : ")))
