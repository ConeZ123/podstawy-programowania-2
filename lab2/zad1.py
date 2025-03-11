# znajdowaie dzielnikow i sprawdzanie perwszosci liczby

# znajdowanie dzielnikow, ktore dziela sie przez n bez reszty

def znajdzDzielnik(n: int)->list[int]:
    dzielniki = []
    for i in range(1, n+1):
        if n % i == 0:
            dzielniki.append(i)
    return dzielniki
        
print(znajdzDzielnik(5))
