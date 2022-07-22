# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    
#     *Пример:*
    
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

from random import randint, random

n = randint(1,100)
print(n)
def number(n):
    l = ''
    while n > 0:
        l += str(n % 2)
        n = n // 2 
    return l[::-1]
print(number(n))

# def DecToBin(n):
#     lstBin = []
#     while n > 0:
#         lstBin.append(str(n%2))
#         n //= 2
#     return "".join(lstBin[::-1])

# print(DecToBin(6))

# def Bin(n):
#     s = bin(n)
#     return s.split('b')[1]
# x=int(Bin(n))
# print(x)

