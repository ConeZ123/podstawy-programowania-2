# Algorytm znajdujący największy element w liście

liczby: list = [3, 5, 2, 8, 1]

def sort(lista: list):
    max = liczby[0]
    for i in lista:
        if i > max:
            max = i
    return max

print(sort(liczby))
                


# funkcja znajdzmax(lista)
#   max = lista[0]
#   tworzymy petle dla kazdego elementu z listy
#   jezeli liczba jest wieksza od max
#   max = liczba    