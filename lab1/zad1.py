# Algorytm znajdujący największy element w liście

liczby: list = [3, -5, 2, 8, 1]

def sort(lista: list):
    try:
        max = liczby[0]
        for i in lista:
            if i > max:
                max = i
        return max
    except IndexError:
        return False
    except TypeError:
        return False

print(sort(liczby))
                    

def findMax2(liczby: list[int]) -> int:
    if not liczby:
        return None