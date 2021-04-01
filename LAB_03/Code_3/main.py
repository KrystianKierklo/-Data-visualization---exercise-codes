#zamiast uzupełniać elementy w pętli

lista = []
for element in zakres:
    if warunek_na_elemencie:
        lista.append("coś sie dzieje z" element)

lista2 = ["coś się dzieje z" element for element in zakres if warunek_na_element]


lista_a = []

for x in range(10):
    lista_a.append(x**2)
print(lista_a)

a = [x**2 for x in range(10)]
print(a)

lista_b = []
for y in range(6):
    lista_b.append(3**y)
print(lista_b)

b = [3**y for y in range(6)]
print(lista_b)

lista_c = []
for z in lista_a:
    if z % 2 == 1:
        lista_c.append(z)
print(lista_c)

c = [z for z in a if z % 2 == 1]
print(lista_c)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_parzyste = []

for a in lista:
    if a % 2 == 0:
        lista_parzyste.append(a)
print(lista_parzyste)

parzyste = [a for a in lista if a % 2 == 0]
print(parzyste)

lista = []
for a in [1, 2, 3]:
    for b in [4, 5, 6]:
        lista.append((a,b))
print(lista)

lista2 = [(i,j) for i in [1, 2, 3] for j in [4, 5, 6]]
print(lista2)

skroty = {"PZU": "Państwowy zakład ubezpieczeń",
          "ZUS": "Zakład ubezpieczeń społecznych",
          "PKO": "Państwowa kasa oszczędnościowa"}

odwrocone = {}
print(skroty)
for  key,value in skroty.items():
    odwrocone[value] = key

print(odwrocone)

slownik_odwrocone = {value: key for key, values in skroty.items()}
print(slownik_odwrocone)

#Funkcje
def nazwa_funkcji(arg_pozycyjne, arg_domyslne = wartosc, *arg, **arg):
    instrukcje
    return wartość
nazwa_funkcji()
from math import *
def rownanie_kwadratowe(a , b , c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("brak pierwiastków")
        return 0
    if delta == 0:
        print("Jeden pierwiastek")
        x = (-b)/(2*a)
        return x
    else:
        print("dwa pierwiastki")
        x1 = (-b - sqrt(delta))/(2*a)
        x2 = (-b + sqrt(delta))/(2*a)
        return x1, x2

print(rownanie_kwadratowe(6, 1, 3))
print(rownanie_kwadratowe(1, 2, 1))
print(rownanie_kwadratowe(1, 4, 1))

from math import *
def dlugosc_odcinka(x1=0, y1=0, x2=0, y2=0):
    return sqrt((x2-x1)**2 + (y2-y1)**2)
#dla argumentow domyslnych
print(dlugosc_odcinka())

#dla argumentow pozycyjnych
print(dlugosc_odcinka(1,2,3,4))

#dwa pierwsze argumenty w kolejnosc, dwa kolejne bez kolejnosci
print(dlugosc_odcinka(2,2,y2=2,x2=1))

print(dlugosc_odcinka(x2=5,y1=2,x1=2,y2=6))

print(dlugosc_odcinka(x2=5,y2=5))

def ciag(*liczby):
    if len(liczby) == 0:
        return 0
    else:
        suma = 0
        for a in liczby:
            suma += a
        return suma

print(ciag())

print(ciag(1,2,3,4,5,6,7))

def to_lubie(**rzeczy):
    for cos in rzeczy:
        print("to jest")
        print(cos)
        print("co lubie")
        print(rzeczy[cos])

to_lubie(slodycze= 'czekolada', rozrywka = ['gry','filmy'])

#moduly & pakiety
from teksty import *

a = "Ala ma kota"

litery.wyswietl(a)
print(litery.dlugosc(a))








