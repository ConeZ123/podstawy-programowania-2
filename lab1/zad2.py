# algorytm Euklidesa
 
# wersja iteracyjna
def euk(a: int, b: int):
    while a != b:
        if a > b:
            a -= b
        if b > a:
            b -= a
    return a

print(euk(8, 26))
