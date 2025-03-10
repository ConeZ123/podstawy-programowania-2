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

test_values = [
        (315, 504),
        (1230, 528),
        (28, 8),
        (12, 18),
        (10000, 1)
    ]

def eukModIter(a, b):
    while b != 0:
        c = a % b 
        a = b
        b = c
    return a

def eukModRec(a, b):
    if b == 0:
        return a
    else:
        return eukModRec(b, a % b)

print("Iteracja: ")
for a, b in test_values:
    print(f"NWD({a}, {b}) = {eukModIter(a, b)}")

print("\nRekurenja:")
for a, b in test_values:
    print(f"NWD({a}, {b}) = {eukModRec(a, b)}")