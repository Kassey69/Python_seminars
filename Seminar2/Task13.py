# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

import random

n = random.randint(4,5)

def hisl(n):
    num = 1
    print(1, end=' ')
    for i in range(1, n+1):
        num *= (-3)   # 1 * -3 = -3; -3 * -3 = 9
        print(num, end=' ')
    return num
hisl(n)
print("")

import random

n = random.randint(4,5)

def hisl(n):
    l = [1]
    num = 1
    for i in range(1, n+1):
        num *= (-3)   # 1 * -3 = -3; -3 * -3 = 9
        l.append(num)
    print(l)
    return num
hisl(n)

# N = int(input('Введите число \n'))
def gira(n):
    for i in range(n+1):
        result = (-3)**i        #   выражение (-3)**0  = 1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print(result, end=' ')
    return result
gira(n)

