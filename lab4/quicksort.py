def quickSort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        mniejsze = [] 
        wieksze = []
        for i in arr:
            if i < pivot:
                mniejsze.append(i)
            elif i >= pivot:
                wieksze.append(i)
        return quickSort(mniejsze) + [pivot] + quickSort(wieksze)

print(quickSort([1, 2, 3, 4, 5]))


import random
def quick_sort2(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    lower = [i for i in arr[1:] if i < pivot]
    higher = [i for i in arr[1:] if i >= pivot]
    return quick_sort2(lower) + [pivot] + quick_sort2(higher)

# mediana 3 warosci

nums = [5, 3, 2, 10, 11, 15, 1, 7]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right) 

arr = [5, 3, 1, 6, 2, 3, 4, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)


def quicksort_index(arr):
    arr = [(value, index) for index, value in enumerate(arr)]
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for index in arr if x < pivot]
    middle = [x for index in arr if x == pivot]
    right = [x for index in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right) 


employees = [
    {"first_name": "Anna", "last_name": "Kowalska", "age": 29},
    {"first_name": "Jan", "last_name": "Nowak", "age": 34},
    {"first_name": "Marek", "last_name": "Kowalski", "age": 25},
    {"first_name": "Zofia", "last_name": "Nowak", "age": 29},
]

# last_name, age
def sort_employees():
    ...



arr = [4, 2, 2, 8, 3, 3, 1]

# napisz funkcje ktora sortuje oceny studentow w zakresie od 0 do 100
# wartosci wchodzace, lista ocen, min wartosc, max wartosc
# wyjscie - posortowane oceny

ocena = [88, 92, 75, 83, 90, 92, 60, 85, 90]

def sortGrades(arr: list, min_value: int, max_value: int) -> list[int]:
    count = [0] * (max_value - min_value + 1)
    for grade in arr:
        count[grade - min_value] += 1
        