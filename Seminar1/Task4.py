# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# import random
# n = round(random.uniform(1, 10), 2)
# print(n)
# def drob(n):
#     return int((n*10) % 10)
# print(drob(n))

import random

def drobs(n):
    n = round(n - int(n),2)
    n = str(n).replace('.','')
    print(n)
    return (int(str(n[1])))

n = round(random.uniform(1, 10), 2)
print(n)
print(drobs(n))

