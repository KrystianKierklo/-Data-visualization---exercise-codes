import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2015', periods=1000))
#
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()
#
# data = {'Kraj': ['Belgia', 'Indsie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brazylia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467]}
#
# df = pd.DataFrame(data)
# print(df)
#
# grupa = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})
# print(grupa)
#
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Kontynent')
# wykres.set_ylabel('Mld')
# wykres.legend()
#
# plt.xticks(rotation=0)
# plt.savefig('Wykres.png')
# plt.title('Populacja z podzialem na kontynenty')
# plt.show()
#
# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
# grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia': ['sum']})
# print(grupa)
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6,6), legend=(0,0))
# plt.legend(loc='lower right')
# plt.title('Suma zamowienia dla sprzedawcy')
# plt.show()
#
# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2015', periods=1000))
#
# ts = ts.cumsum()
#
# df = pd.DataFrame(ts)
#
# df['MA'] = df.rolling(window=50).mean()
# df.plot()
# plt.show()

#################################################################################
#################################################################################

# plt.plot([1, 2, 3, 4])
# plt.ylabel('jakies liczby')
# plt.show()
#
# plt.plot([1, 2, 3, 4], [1, 4, 8, 16], 'ro-')
#
# plt.axis([0, 6, 0, 20])
#
# plt.show()
#
# plt.plot([1, 2, 3, 4], [1, 4, 8, 16], 'r')
# plt.plot([1, 2, 3, 4], [1, 4, 8, 16], 'o')
#
# plt.axis([0, 6, 0, 20])
#
# plt.show()
#
# t = np.arange(0., 5., 0.2)
#
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()
#
# x = np.linspace(0, 2, 100)
#
# plt.plot(x, x, label='postac liniowa')
# plt.plot(x, x**2, label='postac kwadratowa')
# plt.plot(x, x**3, label='postac szescienna')
#
# plt.xlabel('etykieta x')
# plt.ylabel('etykieta y')
# plt.title('Prosty wykres')
# plt.legend()
#
# plt.show()
#
# x = np.arange(0, 10, 0.1)
# s = np.sin(x)
# plt.plot(x, s, label='sin(x)')
#
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykres sin(x)')
# plt.legend()
#
# plt.show()

x1 = np.arange(0.0, 2.0, 0.02)
x2 = np.arange(0.0, 2.0, 0.02)

y1 = np.sin(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x1)

plt.subplot(2, 1, 1)
plt.plot(x1, y1, '-')
plt.title('Dwa podwykresy')
plt.ylabel('sin(x)')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r-')
plt.xlabel('x')
plt.ylabel('cos(x)')

plt.show()
