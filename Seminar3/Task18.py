# 3. Задайте список из n чисел ряда фибоначи и выведите на экран их сумму.
    
#     *Пример:*
    
#     -  n = 10     1 1 2 3 5 8 13 21 34 55 

# 1. мой вариант
import random

n = random.randint(5,10)
print(n)
def fib(n):
    l = [1,1] # из этих двух чисел формируются последующие, начиная с 3 элемента range(2, n)
    result = 1
    for i in range(2, n): 
       result = l[-1] + l[-2] # обознгачение сложение двух предыдущих значений
       l.append(result) 
    return l
print(fib(n)) # 1 2 3 4 5 6 


# 2 вариант
# def fibo(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# x = int(input('Введите число элементов: '))


# def fibolist(x):
#     list = []
#     for i in range(1, x+1):
#         list.append(fibo(i))
#     return list
# print(fibolist(x))






