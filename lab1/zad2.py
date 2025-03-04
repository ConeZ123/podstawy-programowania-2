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

# wersja rekurencyjna
def eukR(a: int, b: int):
    if a == b:
        return a
    if a > b:
        return eukR(a-b , b)
    else:
        return eukR(a, b-a)
    
print("NWD rekurencyjnie:", eukR(8, 26))

# wersja modulo (iteracyjnie i rekurencyjnie)
