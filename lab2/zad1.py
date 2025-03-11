import timeit
import math

# znajdowaie dzielnikow i sprawdzanie perwszosci liczby
# znajdowanie dzielnikow, ktore dziela sie przez n bez reszty

def znajdzDzielnik(n: int)->list[int]:
    dzielniki = []
    for i in range(1, n+1):
        if n % i == 0:
            dzielniki.append(i)
    return dzielniki
        
print(znajdzDzielnik(5))

def znajdzDzielnik2(n: int) -> list[int]:
    return [i for i in range(1, n+1) if n % i == 0]

def znajdzDzielnik3(n: int) -> list[int]:
    return [i for i in range(1, n // 2+1) if n % i == 0]

n = 10 ** 6
print("1: ", timeit.timeit(lambda: znajdzDzielnik(n), number=1), "sekundy")
print("2: ", timeit.timeit(lambda: znajdzDzielnik2(n), number=1), "sekundy")
print("3: ", timeit.timeit(lambda: znajdzDzielnik3(n), number=1), "sekundy")
print("4: ", timeit.timeit(lambda: znajdzDzielnik4(n), number=1), "sekundy")

def znajdzDzielnik4(n: int) -> list[int]:
    dzielniki = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            dzielniki.append(i)
            dzielniki.append(n // i)
    return dzielniki

# znajdz najwiekszy dzielnik

def znajdzNajwiekszyDzielnik(n: int) -> list[int]:
    dzielniki = []

    for i in range(1 , n+1):
        if n % i == 0:
            dzielniki.append(i)
            max = dzielniki[0]
            if i > max:
                max = i
                dzielniki.clear()
                dzielniki.append(max)
    return dzielniki

print(znajdzNajwiekszyDzielnik(100))