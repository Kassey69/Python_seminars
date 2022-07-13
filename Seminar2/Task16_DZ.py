# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# на платформу скинуть скрины выполнения программы + в комменте ссылку на гитхаб.

from random import randint

n = randint(3,10)
print(n)
def number(n):
    l = []
    resilt = 1
    for i in range(1,n+1):
        resilt *= i
        l.append(resilt)
    print(l)
    return l
number(n)