# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Дополниьтельно - разделения целого числа на цифры в Python ниже после задачи.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math
import random
# при делении всегда нужно использовать import math  и mmath.floor или math.ceil
# метод floor() в Python возвращает значение floor из x, то есть наибольшее целое число, не превышающее x.
# Метод ceil(x) в Python возвращает максимальное значение x, то есть наименьшее целое число, большее или равное x.
# math.ceil()Функция округляет число до целого числа. math.log()Функция предоставляет натуральный логарифм числа. 

number = random.randint(3,10)
n = [random.randint(3,10) for i in range(number)]
print(n)

def par_num(n):
    return [n[-1-i] * n[i] for i in range(math.ceil(len(n)/2))]
print(par_num(n))





def par_num(n):
    l = []
    result = 0
    for i in range(math.ceil(len(n)/2)): # при math.floor получится [12, 15]
        result = n[-1-i] * n[i]
        l.append(result)
    return l
# print(par_num(n))



# Полезно с задаче никакого отношения не имеет
# Следующий код использует понимание списка для разделения целого числа на цифры в Python.

# num = 13579
# x = [int(a) for a in str(num)]
# print(x) # [1, 3, 5, 7, 9]


# import math
# n = 13579
# x = [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]
# print(x) # [1, 3, 5, 7, 9]


# # Следующий код использует функции map()и str.split()для разделения целого числа на цифры в Python.

# str1 = "1 3 5 7 9"
# list1 = str1.split()
# map_object = map(int, list1)

# listofint = list(map_object)
# print(listofint)  # [1, 3, 5, 7, 9]