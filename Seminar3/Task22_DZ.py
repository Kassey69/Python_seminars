# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# n = [2, 3, 5, 9, 3] 
from random import randint
n = randint(5,10)
My_list = [randint(1,10) for i in range(n)]
print(My_list)

def number(number):    
    return [number[i] for i in range(len(number)) if i % 2 != 0]
print(f'Элементы стоящие на нечётных позициях:', number(My_list))
print(f'Cумма элементов списка =', sum(number(My_list)))
    





# def number(number):
#     # sum = 0
#     # for i in range(len(n)):
#     #     if i % 2 != 0:         
#     #         sum += number[i]     
#     return [number[i] for i in range(len(number)) if i % 2 != 0]
# print(f'Элементы стоящие на нечётных позициях:', number(My_list))
# print(f'Cумма элементов списка =', sum(number(My_list)))