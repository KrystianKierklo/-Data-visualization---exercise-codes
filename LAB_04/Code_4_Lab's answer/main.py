#Zad1
lista = [a * 2 for a in range(0,31)]
print(lista)
plik = open('Zadanie1.txt','w')
plik.writelines(str(lista))
plik.close()

Zad2
plik = open('Zadanie1.txt','r')
zawartosc = plik.read()
print(zawartosc)
plik.close()

#Zad3
with open('Zadanie1.txt', 'r+') as plik:
    plik.write("Zapisany tekst do pliku")


zapis został dokonany od początku pliku, po zapisaniu komunikatu do pliku
wskaźnik został przesuniety o zadaną długość naszego komunikatu (przy trybie r+)
a następnie zostały odczytane dane z pliku, aby odczytać całą zawartość pliku
najlepiej zamknąć plik i otworzyć go ponownie,
przy trybie w+ jeśli plik istnieje jest czyszczony podczas otwarcia
przy trybie a+ jeśli plik istnieje i chcemy z niego odczytać dane, za pomocą metody seek(0)
z argumentem 0 ustawiamy obecną pozycję w pliku

with open('Zadanie1.txt', 'a+') as plik:
    plik.seek(0)
    zawartosc = plik.read()
print(zawartosc)
#Zad4
class NaZakupy():
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print("produkt to {}, w ilości {}{}, przy cenie {}zł za {}".format(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed, self.jednostka_miary))

    def ile_produktu(self):
        print("{} {}".format(self.ilosc, self.jednostka_miary))

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

produkt = NaZakupy("Ziemiaki", 3, "kg", 2)
produkt.wyswietl_produkt()
produkt.ile_produktu()
print(str(produkt.ile_kosztuje()) + " zł")
produkt1 = NaZakupy("Gazeta", 2, "szt.", 3)
produkt1.wyswietl_produkt()
#Zad5
class CiagArytmetyczny():
    def __init__(self):
        self.a1 = None
        self.r = None
        self.n = None
        self.ciag = []

    def wyświetl_dane(self):
        for elem in self.ciag:
            print(elem)

    def pobierz_elementy(self):
        while True:
            element = input("Podaj liczbę lub wpisz 'koniec': ")
            if element != 'koniec':
                self.ciag.append(float(element))
            else:
                break

    def pobierz_parametry(self):
        a = input("Wprowadź parametr a: ")
        self.a1 = int(a)
        r = input("Wprowadź parametr r: ")
        self.r = int(r)
        n = input("Wprowadź parametr n: ")
        self.n = int(n)


    def policz_sume(self):
        return sum(self.ciag)

    def policz_elementy(self):
        if (self.a1 is not None) & (self.r is not None) & (self.n is not None): # lub if None not in self.__dict__.values():
            indeks = 1
            self.ciag.append(self.a1)
            while indeks != self.n:
                self.a1 += self.r
                self.ciag.append(self.a1)
                indeks += 1



ciag = CiagArytmetyczny()
ciag.pobierz_parametry()
ciag.policz_elementy()
ciag.wyświetl_dane()
print(ciag.policz_sume())

#zad.6

class Robaczek():
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    def idz_w_gore(self, ile_krokow):
        self.y = self.y + (ile_krokow * self.krok)
        self.x = self.x
    def idz_w_dol(self, ile_krokow):
        self.y = self.y - (ile_krokow * self.krok)
        self.x = self.x
    def idz_w_lewo(self, ile_krokow):
        self.y = self.y
        self.x = self.x - (ile_krokow * self.krok)
    def idz_w_prawo(self, ile_krokow):
        self.y = self.y
        self.x = self.x + (ile_krokow * self.krok)
    def pokaz_gdzie_jestes(self):
        print("współrzędne robaczka to x={} y={}".format(self.x, self.y))
robak = Robaczek(1,0,1)
robak.pokaz_gdzie_jestes()
robak.idz_w_gore(5)
robak.pokaz_gdzie_jestes()
robak.idz_w_lewo(3)
robak.pokaz_gdzie_jestes()
robak.idz_w_dol(2)
robak.pokaz_gdzie_jestes()
robak.idz_w_prawo(4)
robak.pokaz_gdzie_jestes()