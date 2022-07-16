# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

import random

n = random.randint(1,2) # выбор целых или дробных чисел
if n == 1:
    n = round(random.uniform(1, 100),2)
else: n = random.randint(1,9999)
print(f'Принимается число на вход: {n}')

def number(n):
    result = 0
    n = list(str(n).replace('.','')) # ['4', '1', '9', '8']
    print(n)
    for i in n:
        i = int(i) # меняем строку в целое число
        result += i # складываем числа 
    print(f'Сумма цифр числа: {result}')
    return result
number(n)