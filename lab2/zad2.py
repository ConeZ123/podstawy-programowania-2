# liczby pierwsze
# n > 2

def prime(n: int):
    if n < 2:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True
        
print(prime(7))