def n_wyraz_ciag_geom(a1,q,n):
    an = a1 * q ** (n-1)
    return an

def suma_n_wyrazow_geom(a1,q,n):
    if q == 1:
        suma = a1 * n
        return suma
    else:
        suma = a1 * ((1-q**n)/(1 - q))
        return suma