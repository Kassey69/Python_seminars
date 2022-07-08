# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

import random
# n =  random.randint(5, 30)
n =  int(input(f'Вебите\n'))
def function(n):
    print (n)
    if ((n % 5 == 0 and n % 10 == 0) or n % 15 == 0) and (not n % 30 == 0):
        print('кратно')
    else: print(' не кратно ')
    return n
function(n)