# Algorytm znajdujący największy element w liście

liczby: list = [3, 5, 2, 8, 1]

def sort(lista: list):
    max = liczby[0]
    for i in lista:
        if i > max:
            max = i
    return max

print(sort(liczby))
                    