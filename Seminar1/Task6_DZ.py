# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# import random

def day_week(n):
    if n > 0 and n <= 7:
        if n > 0 and n <=5:
            print(f'будний день {n}')
        elif n>=6 and n < 8:
            print(f'выходной {n}')
    else:
         print(f'день введен некорректно {n}')
    return n

# n = random.randint(1,10)
n = int(input(f'Введите день недели \n'))
day_week(n)