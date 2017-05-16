# Алгоритм Евклида: ищет НОД двух чисел
def evklid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b

# Примеры
print(evklid(*[int(x) for x in input().split()]))
