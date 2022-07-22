# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.
    
#     *Пример:*
    
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

import math
import random
# при делении всегда нужно использовать import math  и mmath.floor или math.ceil
# метод floor() в Python возвращает значение floor из x, то есть наибольшее целое число, не превышающее x.
# Метод ceil(x) в Python возвращает максимальное значение x, то есть наименьшее целое число, большее или равное x.
# math.ceil()Функция округляет число до целого числа. math.log()Функция предоставляет натуральный логарифм числа. 

number = random.randint(3,10)
n = [random.randint(3,10) for i in range(number)]
print(n)

# def par_num(n):
#     return [n[-1-i] * n[i] for i in range(math.ceil(len(n)/2))]
# print(par_num(n))

def par_num(n):
    l = []
    result = 0
    for i in range(math.ceil(len(n)/2)): # при math.floor получится [12, 15]
        result = n[-1-i] * n[i]
        l.append(result)
    return l
print(par_num(n))