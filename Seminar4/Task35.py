# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    
#     *Пример:*
    
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1,

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


# def fibo(n):
#     fibo_list = list()
#     fibo_list.append(0)
#     fibo_list.append(1)
    
#     for i in range(2, n+1):
#         fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])
    
#     fibo_list.insert(0, 1)
#     fibo_list.insert(0, -1)

#     for i in range(0, n-2):
#         fibo_list.insert(0, (fibo_list[1]) - (fibo_list[0]))
#     return fibo_list

# x = fibo(10)
# print(x)








# x = []
# integer = []
# result = []
    
# x = list(str(a))[::-1]
    
    
# while True:
#     if a != 0:
#         if a % 2 == 0:
#             result.append(0)
#             a = a // 2
#         elif a % 2:
#              result.append(1)
#              a = a // 2
#     else:
#         result.reverse()
#         print(result)
#         break
# input()


