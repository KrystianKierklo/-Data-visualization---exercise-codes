import numpy as np

a = np.array([20, 30, 40 ,50])
b = np.arange(4)

print(a)
print(b)

# wykonane bedzie dzialanie i zapisanie wyniku do nowej zmiennej
c = a - b
print(c)

# wykonanie operacji kwadrat zawartosci
print(b ** 2)

# mozemy zmodyfikowac zawartosc tablicy a, pamietamy ze elementy beda przechowywane po modyfikacji
a += b
print(a)
a -= b
print(a)

a = np.arange(12).reshape(3,4)

print(a)

# suma calej macierzy
print(a.sum())

# suma kazdej z kolumn
print(a.sum(axis=0))

# minimalna dla kazdego z wierszy
print(a.min(axis=1))

# suma skumulowana dla wierszy
print(a.cumsum(axis=1))

a = np.arange(3)
b = np.arange(3)

print(a)
print(b)
print(a.dot(b))
print(np.dot(a,b))

a = np.array([[2, 1, 3], [-1, 2, 4]])
b = np.array([[1, 3], [2, -2], [-1, 4]])

print(a)
print(b)
print(a.dot(b))

a = np.ones(3, dtype='int32')
print(a)
print(a.dtype)
b = np.linspace(0, np.pi, 3)
print(b)
print(b.dtype)

c = a + b
print(c)
print(c.dtype)

d = np.exp(c*1j)
print(d)
print(d.dtype)


b = np.arange(3)

print(b)
print(np.exp(b))
print(np.sqrt(b))

c = np.array([2., -1., 4.])
print(np.add(b, c))

a = np.arange(6).reshape(3,2)
print(a)
for b in a.flat:
    print(b)
    print("")

# romiary macierzy 1x6. 1 x ilosc elementow w tablicy jednowymiarowej
a = np.arange(6)
print(a)
print(a.shape)

b = a.reshape((3, 2))
print(b)
print(b.shape)
print("")
c = a.reshape((2,3))
print(c)
print(c.shape)

d = c.ravel()
print(d)

e = c.T
print(e)
print(e.shape)
