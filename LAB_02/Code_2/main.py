#listy

lista = ['s', 3, 4.5, 1, 2, [3, 4, 5]]
print(lista)

lista.append('slowa')
lista.append(5)
print(lista)

lista.insert(3, 6)
print(lista)
lista.insert(15, 5)
print(lista)

lista.pop()
print(lista)

lista.pop(1)
print(lista)

lista.remove('s')
print(lista)

del lista[5]
print(lista)

lista.reverse()
print(lista)

lista.extend((2, 2, 5))
print(lista)

lista_nowa = [5, 2, 1, 8, 3.2, 3.05, 6, 4]
lista_nowa.sort()
print(lista_nowa)


#slowniki

slownik = {2: 's', 'ab': 'df', 3.4: 45, 2: 3}
print(slownik)

slownik['klucz'] = 'wartosc'
slownik[6] = 2
print(slownik)

print(slownik['ab'])

slownik.pop(6)
print(slownik)

print(slownik.keys())
print(slownik.values())

del slownik[2]
print(slownik)

#wstawianie

napis = input("Wpisz jakas litere: ")
print(napis)
print(type(napis))

liczba = input("wprowadz liczbe: ")
print(liczba)
print(type(liczba))
liczba = float(liczba)
print(type(liczba))

import sys as system

system.stdout.write("wprowadz literę: ")
litera = system.stdin.readline()
system.stdout.write(litera)

#warunkowe itp

if warunek:
    instrukcje
elif warunek1:
    instrukcje

else:
    instrukcje

a = input('wprowadz liczbe a: ')
b = input('wprowadz liczbe b: ')

a = int(a)
b = int(b)

if a > b:
    print('liczba ' + str(a) + ' jest wieksza')
elif a < b:
    print('liczba ' + str(b) + ' jest wieksza')
else:
    print("liczby sa rowne")


if a==b:
    print('liczby sa rowne')
else:
    print('liczby nie sa rowne')

a = input('wprowadz liczbe a: ')
b = input('wprowadz liczbe b: ')
c = input('wprowadz liczbe c: ')
d = input('wprowadz liczbe d: ')

a = int(a)
b = int(b)
c = int(c)
d = int(d)

if (a > b) & (c > d):
    print("liczba a jest wieksza od liczby b i liczba c jest wieksza od liczby d ")
else:
    print("liczba a jest mniejsza od liczby b lub liczba c jest mniejsza od liczby d")


#petle

for liczbik in sekwencja:
    instrukcja
else:

range(1,6,1)

for x in range(1, 6, 1):
    print(x)
else:
    print("petla zakonczyla dzialanie")

lista = [3, 4, 5, 1, 5]
for x in lista:
    print(x)

while warunek:
    instrukcja
else:


z = 0
while z != 10:
    print(z)
    z += 1
else:
    print('zostalo wyswietlonych ' +str(z) + ' liczb')

lista = [4, 6, 2, 3, 5, 9, 1]

liczba = input('wprowadz liczbe: ')

licznik = 0

while licznik < len(lista) - 1:
    if int(liczba) - lista[licznik] == 0:
        print(liczba + ' -' + str(lista[licznik]) + ' =0')
        break
    else:
        print(lista[licznik])
        licznik += 1

lista = [4, 6, 2, 3, 5, 9, 1]
lista2 = [7, 3, 4, 6]
suma = []

for a in lista:
    for b in lista2:
        wynik = a + b
        suma.append(wynik)
    print(suma)

#bledy

try:
    instrukcje
except

a = input("wpisz liczbe a: ")
b = input('wpisz liczbe b: ')

try:
    wynik = int(a) / int(b)
    print(wynik)
except ZeroDivisionError:
    print('tylko Chuck Norris moze dzielic przez zero')


