import numpy as np

a = np.arange(2)
print(a)

a = np.array([0, 1, 2])
print(a)
print(type(a))
print(a.dtype)

a = np.arange(2, dtype='int64')
print(a)
print(a.dtype)

b = a.astype('float')
print(b)
print(b.dtype)
print(b.shape)
print(b.ndim)

m = np.array([np.arange(2), np.arange(2)])
print(m)
print(m.ndim)

zero = np.zeros((5,5))
jedynki = np.ones((4,4))
print(zero)
print(jedynki)

pusta = np.empty((2,2))
print(pusta)

poz_1 = pusta[1, 1]
poz_2 = pusta[0, 1]
print(poz_1)
print(poz_2)

macierz = np.array([[1, 2], [3,4]])
print(macierz)

liczby = np.arange(1, 2, 0.1)
print(liczby)

liczby_lin = np.linspace(1, 2, 5, endpoint=False)
print(liczby_lin)

z = np.indices((5, 3))
print(z)

x, y = np.mgrid[0:5, 0:5]
print(x)
print(y)

mat_diag = np.diag([a for a in range(5)], k=-1)
print(mat_diag)

z = np.fromiter(range(5), dtype='int32')
print(z)

marcin = b'Marcin'
mar_1 = np.frombuffer(marcin, dtype='S1')
print(mar_1)
mar_2 = np.frombuffer(marcin, dtype='S2')
print(mar_2)

marcin = "Marcin"
mar_3 = np.array(list(marcin))
print(mar_3)
print("")
mar_4 = np.array(list(marcin), dtype='S1')
print(mar_4)
print("")
mar_5 = np.array(list(b'Marcin'))
print(mar_5)
print("")
mar_6 = np.fromiter(marcin, dtype='S1')
print(mar_6)
print("")
mar_7 = np.fromiter(marcin, 'U1')
print(mar_7)

mat = np.ones((2, 2))
mat_1 = np.ones((2, 2))
print(mat + mat_1)
print(mat - mat_1)

mat_2 = np.array([[4,6], [8, 10]])
mat_3 = np.array([[2, 2], [2, 2]])
print(mat_2 * mat_3)
print(mat_2 / mat_3)

a = np.arange(10)
print(a)

s = slice(2, 7, 2)
print(a[s])

s = range(2, 7, 2)
print(a[s])

print(a[2:7:2])

print(a[1:])
print(a[2:5])

mat = np.arange(25)

mat = mat.reshape((5, 5))
print(mat)
print(mat[1:])
print(mat[:, 1])
print(mat[:, 1:2])
print(mat[2:5, 1:3])
print(mat[:, range(2, 5, 2)])

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)

rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])

y = x[rows, cols]
print(y)
