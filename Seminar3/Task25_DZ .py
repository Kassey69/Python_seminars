# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

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



# number = int(input('Число введите: '))
# numberb = ''
# while number > 0:
#     numberb = str(number % 2) + numberb
#     number = number // 2
 
# print(numberb)
