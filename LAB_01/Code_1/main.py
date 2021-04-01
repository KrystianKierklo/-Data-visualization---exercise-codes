from math import *
#zad2
pierwsza_liczba = input("Podaj pierwszą liczbę: ")
znak = input("Podaj znak działania: ")
druga_liczba = input("Podaj drugą liczbę: ")


if znak == "+":
    suma = int(pierwsza_liczba) + int(druga_liczba)
    print(suma)
elif znak == "-":
    roznica = int(pierwsza_liczba) - int(druga_liczba)
    print(roznica)
elif znak == "*":
    iloczyn = int(pierwsza_liczba) * int(druga_liczba)
    print(iloczyn)
elif znak == "/":
    iloraz = int(pierwsza_liczba) / int(druga_liczba)
    print(iloraz)
else:
    print("error")

#zad4
a = exp(10)

print(a)
sinus = sin(8)**2
logarytm = log(5 + sinus) ** (1/6)
# b = pow(logarytm, 1/6)
print(logarytm)

c = floor(3.55)
print(c)
d = ceil(4.8)
print(d)
#zad5
imie = "RADOSŁAW"
nazwisko = "CYBULSKI"
print(imie.capitalize() + " " + nazwisko.capitalize())
#Zad6
napis = "la la la la"
print(napis.count("la"))
#Zad7
napis1 = "teskst do sprawdzenie"
print(napis1[1], napis1[len(napis1)-1])
#Zad8
print(napis.split())
#Zad9
napis2 = "Jest dziś poniedziałek"
print("Jaki mamy dziś dzień? %s " %  (napis2))
liczba = 5.677
print("twoja liczba to: %(z1).2f" % {'z1': liczba})
liczba_szesnastkowo = 0xf351
print(liczba_szesnastkowo)
print("%x" % (liczba_szesnastkowo))


