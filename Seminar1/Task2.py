# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

import random

def spisok():
    n = random.randint(4,10)
    l = []
    for i in range(n):
        l.append(random.randint(-100, 100))
    return l

def maxs(l):
    max = 0
    for i in l:
        if i > max:
            max = i
    return max

f = spisok()
print(f)
print(maxs(f))