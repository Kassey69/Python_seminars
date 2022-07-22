# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.


import random

def number(num):
    return [random.randint(1,90) for i in range(num)]   

n = random.randint(4,21)
Mu_List = number(n) # тут мы значение функции рандомного числа переписываем в будущий список
Mu_List2 = str(Mu_List).replace(',', '') #сдесь мы убираем все запятые и меняем на пробелы как просили
print(Mu_List2)
print(f'Минимальный элемент: [{min((Mu_List))}], Максимальный элемент: [{max((Mu_List))}]')
print("")

import random

def number(num):
    num = random.randint(4,21)
    return [random.randint(1,90) for i in range(num)]   

def min_max(Stroka):
    mins = Stroka[0]
    maxs = Stroka[0]
    for i in range(len(Stroka)):
        if mins > Stroka[i]: mins = Stroka[i]
        elif maxs < Stroka[i]: maxs = Stroka[i]
    else: print(f'Минимальный элемент: [{mins}], Максимальный элемент: [{maxs}]')
    return [mins, maxs] # функция для выделения каждого элемента из списка для 
                                                    # нахождения минимального и максимального элемента
Mu_List = []
Mu_List = number(str(Mu_List).replace(',', '')) # сдесь мы убираем все запятые и меняем на пробелы как просили
print(Mu_List)
min_max(Mu_List)








# a = input('введите числа через пробел: ')

# def num (a):
#     f = [int(s) for s in a.split()]
#     print(f)
#     print(min(f),max(f))

# num(a)
