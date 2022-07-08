# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
#     *Примеры:* 
    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

import random
n =  random.randint(2, 10)
print(n)
def nums(n):
    for i in range(-n,n+1):
        print(i,end=' ')
    return n
nums(n)