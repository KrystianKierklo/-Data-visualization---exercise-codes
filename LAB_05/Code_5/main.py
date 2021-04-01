class Ksztalty:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.opis = "To jest klasa dla ogolnych ksztaltow"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, tekst):
        self.opis = tekst

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.y = self.y * czynnik

class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __str__(self):
        return "Kwadrat o dlugosci boku rownym {}".format(self.x)

class KwadratLiteraL(Kwadrat):

    def pole(self):
        return 3 * self.x * self.y

    def obwod(self):
        return 12 * self.x


kwadrat = Kwadrat(5)
print(kwadrat.pole())
print(kwadrat.obwod())
kwadrat.dodaj_opis("Nasza figura to kwadrat")
print(kwadrat.opis)
kwadrat.skalowanie(0.3)
print(kwadrat.x)
print(kwadrat.pole())

kwadrat_l = KwadratLiteraL(5)
print(kwadrat_l.pole())
print(kwadrat_l.obwod())
kwadrat_l.dodaj_opis("Sa trzy kwadraty w ksztalcie litery L")
print(kwadrat_l.opis)
kwadrat_l.skalowanie(0.3)
print(kwadrat_l.pole())

kwadrat = Kwadrat(5)
print(kwadrat)


#Atrybuty globalne

class Point:

    counter = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(1,1)

print(p1.counter)
print(p2.counter)
p1.update(1)
print(p1.counter)
print(p2.counter)

class Pracownik:
    pass

janek = Pracownik()
janek.imie = "Janek"
janek.nazwisko = "Kowalski"
janek.wiek = 30

class Pracownik:

    __prywatna = "tajne haslo"

    def __init__(self, imie):
        self.imie = imie

janek = Pracownik("Janek")
print(janek._Pracownik__prywatna)

class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)

class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        #super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {}, i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadzerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

janek = Pracownik("Janek", "Mikulski", 3000)
adrian = Menadzer("Adrian", "Bajka", 12000)

print(janek.przedstaw_sie())
print(adrian.przedstaw_sie())

class Pracownik():

    def __init__(self, pensja):
        Osoba.__init__(self, imie, nazwisko)
        self.pensja = pensja

    #def przedstaw_sie(self):
    #    return "{} {}, i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

class Menadzer(Osoba, Pracownik):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        Pracownik.__init__(self, pensja)

    def przedstaw_sie(self):
        return "{} {}, jestem menadzerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

print(adrian.przedstaw_sie())

#Iteratory

for element in range(1,11):
    print(element)

imie = "Reks"
it = iter(imie)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

class Wspak:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

obiekt = Wspak("napis")
for a in obiekt:
    print(a)


#Generatory

def reverse(data):
    for a in range(len(data) - 1, -1, -1):
        yield data[a]

gen = reverse("Zdzislaw")
print(gen)
print(next(gen))
print("napis")
print(next(gen))


litery = (litera for litera in "Feliks")
print(litery)
print(next(litery))