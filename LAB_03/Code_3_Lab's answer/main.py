from ciagi import *
Zad1
a = [1-x for x in range(11)]
b = [4**y for y in range(8)]
c = [z for z in b if z % 2 == 0]

print(a)
print(b)
print(c)

Zad2
lista = []
for a in range(10):
    a = random.randrange(500)
    lista.append(a)
print(lista)
parzyste = [b for b in lista if b % 2 == 0]
print(parzyste)

Zad3
produkty = {"paczka ryżu": "sztuka", "jabłka": "kg", "gruszki": "kg", "gazeta": "sztuka"}
lista_produkty = [key for key, value in produkty.items() if value.count("sztuka")]
print(lista_produkty)

Zad4
def trojkat_prostokatny(a,b,c):
    przyprostokatne = a**2 + b**2
    przeciwprostokatna = c**2
    if przyprostokatne == przeciwprostokatna:
        print('trójkąt o podanych rozmiarach jest prostokątny')
    else:
        print('trójkąt o podanych rozmiarach nie jest prostokątny')
trojkat_prostokatny(3,4,5)

Zad5
def pole_trapezu(a=4, b=8, h=3):
    return ((a + b)* h) / 2

Zad6
def ciag(a = 1, b = 4, ile = 10):
    lista = []
    z = 0
    if ile <= 0:
        print('wartość ile nie może być mniejsza od 0')
        return 0
    elif ile == 1:
        return a*b
    else:
        while z != ile:
            a *= b
            lista.append(a)
            z += 1
        return lista
print(ciag())
print(ciag(ile=0))
print(ciag(ile=1))

zad7
def ciag1(* liczby):
    # jeżeli nie ma argumentów to
    if len(liczby) == 0:
        return 0
    else:
        wynik = liczby[0]
        #sumujemy elementy ciągu
        for i in liczby:
            wynik *= i
        #zwracamy wartość sumy
        return wynik
print(ciag1())
print(ciag1(1,2,3,4,5,6,7))

zad8
def lista_zakupow(** produkty):
    return  len(produkty),sum(produkty.values())

print(lista_zakupow(mleko = 2.54, czekolada = 2))

print(arytmetyczny.n_wyraz_ciagu_aryt(5,12,3))
