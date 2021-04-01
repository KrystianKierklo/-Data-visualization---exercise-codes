import sys
#Zad1
filmy = ["Pasażer",
         "Eskorta",
         "Mission: Imposible-Fallout",
         "Krwawy diament",
         "Bad Boys II",
         "Bad Boys",
         "Słaby punkt"
         ]
print(filmy)
filmy.reverse()
print(filmy)


filmy2 = ["Królowie ulicy", "Teoria chaosu", "Bogowie ulicy"]
index = 5
for i in filmy2:
    filmy.insert(index, i)
    index += 1
print(filmy)
premiery = ["11 kwietnia 2007",
            "7 kiwetnia 1995",
            "9 lipca 2003",
            "8 grudnia 2006",
            "12 lipca 2018",
            "3 kwietnia 2008",
            "15 grudnia 2005",
            "8 wrzesnia 2012",
            "15 sierpnia 2008",
            "10 stycznia 2018"
            ]
#Zad2
filmy_slownik = {}
index2 = 0
for a in filmy:
    filmy_slownik[a] = premiery[index2]
    index2
print(filmy_slownik)

#Zad3
przedmioty = {"AM": "Analiza matematyczna",
              "WD": "Wizualizacja danych",
              "MD": "Matematyka dyskretna",
              "PS": "programowanie strukturalne"
              }
print(przedmioty)
print("Słownik zawiera " + str(len(przedmioty)) + " elementy")
#Zad4
liczba = input("Wczytaj liczbę: ")
liczba = float(liczba)
wynik = liczba ** liczba
print(wynik)

#Zad5
sys.stdout.write("Wczytaj tekst: ")
tekst = sys.stdin.readline()
sys.stdout.write(tekst)
sys.stdout.write(str(tekst.count("a")))
sys.stdout.write("\n")
#Zad6
liczba_a = input("Wprowadź liczbę a: ")
liczba_b = input("Wprowadź liczbę b: ")
liczba_c = input("Wprowadź liczbę c: ")

liczba_a = int(liczba_a)
liczba_b = int(liczba_b)
liczba_c = int(liczba_c)

if (liczba_a % 2 == 0) & (liczba_b > liczba_c):
    print("Liczba a jest pażysta i liczba b jest większa niż liczba c")
else:
    print("Liczba a jest nie pażysta lub liczba b jest mniejsza niż liczba c")
#Zad7
liczby = [1, 2, 3, 4, 5, 5.5]

for i in range(0,len(liczby),1):
    if i == 0:
        print(liczby[i])
    else:
        suma = liczby[i] + liczby[i-1]
        print(suma)
#Zad8
z = 0
parzyste = []
while z != 10:
    liczba = input("wpisz liczbę: ")
    liczba = float(liczba)
    if liczba % 2 == 0:
        parzyste.append(liczba)
    z += 1
print(parzyste)
#Zad9
lista2 = [1, 2, 3, 4, 5, 6]

for a in lista2:
    for b in lista2:
        if (a == 1) | (a == 6):
            sys.stdout.write("O")
        else:
            if (b == 1) | (b == 6):
                sys.stdout.write("O")
            else:
                sys.stdout.write(" ")
    sys.stdout.write("\n")
#Zad10
try:
    wprowadzana_liczba = input("wprowadź liczbę: ")
    wprowadzana_liczba = float(wprowadzana_liczba)
    print(wprowadzana_liczba)
except ValueError:
    print("Wprowadzona wartość nie jest liczbą")
a = 5
sys.stdout.write(str(a))
sys.stdout.write("aaaa")
sys.stdout.write('\n')
sys.stdout.write("aaaa")