# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

import random

n = random.randint(6,10)
print(n)
def fib1(n):
    l = [1,1]  
    result = 1
    for i in range(2, n): 
       result = l[-1] + l[-2]  
       l.append(result) 
    return  l

def fib2(n):
    d = [0,1,1]
    result2 = 1
    for i in range(2, n): 
       result2 = d[-1] + d[-2] 
       d.append(result2)  
    return d

def minus(n):
    for i in range(len(n)):
        if i % 2 != 0: n[i] = - n[i] 
    return n

fibo1 = minus(fib1(n))
fibo2 = fib2(n)
print(fibo1[::-1] + fibo2)