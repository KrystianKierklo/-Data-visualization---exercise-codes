operacje na plikach
plik = open(nazwa, tryb, bufor)
plik = open('C:/Users/Krystian/Desktop/123.txt','r')

znaki = plik.read(10)

linia = plik.readline()

linie = plik.readlines()

plik.close()

print(znaki)

print(linia)

print(linie)

import sys
print('Podaj kierunek studiów, rok i specjalizacje: ')

dane = sys.stdin.readline()

plik = open('dane.txt', 'w+', encoding='utf8')

plik.write(dane)

plik.close()

lista = []
for a in range(5):
    lista.append(a)

plik = open('dane.txt', 'a+', encoding='itf8')

plik.writelines(str(lista))

plik.close()


with open('123.txt', 'r') as plik:
    for linia in plik:
        print(linia, end='')


#programowanie obiektowe

class PierwszaKlasa():
    """Jest to pierwsza klasa w pythonie"""
    atrybut = 54321
    def pierwsza_metoda(self):
        return "Teraz działa pierwsza metoda"

obiekt = PierwszaKlasa()
print(obiekt)
print(obiekt.atrybut)
print(obiekt.pierwsza_metoda())
obiekt.tekst = "abcd"
print(obiekt.tekst)

class Kształt():
    __zmienna__ = 'abc'
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, tekst):
        self.opis = tekst

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.y = self.y * czynnik

    def zmieniam_tekst(self, tekst):
        tekst += " to jest"
        return tekst

prostokat = Kształt(10, 30)
print(prostokat.pole())
print(prostokat.obwod())
print(prostokat.opis)
prostokat.dodaj_opis('prostokąt')
print(prostokat.opis)
prostokat.skalowanie(0.5)
print(prostokat.x)
print(prostokat.y)
print(prostokat.pole())
print(prostokat.__zmienna__)

prostokat.__zmienna__ = 'xyz'
print(prostokat.__zmienna__)

print(prostokat.zmieniam_tekst(prostokat.__zmienna__))


