# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# подробное объяснение формулы эвклида - https://www.youtube.com/watch?v=IEORD_eVfCo

import random
import time
# a, b, *_= map(int, input().split()) # ввод значений вручную 
#*_ - мусорная переменная. после этого можно вводить сколько угодно
# map применит в каждому итератору функцию int и запишет введенные значения через пробел

a = random.randint(-10,90)
if a == 0:
    a = random.randint(1,90) # если попали рандом то заново рандом пускаем, но уже без 0
b = random.randint(-10,90)
if b == 0:
    b = random.randint(1,90) # если попали рандом то заново рандом пускаем, но уже без 0
print(f'Вводим данные: {a, b}')

if (a <= 0) or (b <= 0):
    print("данные некорректны, ничего не гарантирую")  # проверяем корректность введенных данных
    # 60 % 48 = 12, 48 % 12 = 12, 12 % 12 = 0 нод = 12
    # 24 и 18:  24 % 18 = 6, 18 % 6 = 0, как только он становится равным нуля то меньшее значение и есть нод = 6
    # 62 и 40:  62 % 40 = 22, 40 % 22 = 18, 22 % 18 = 4, 18 % 4 = 2, 4 % 2 = 0!! нод = 2    
    # 54 и 4:   54 % 4 = 18, 18 % 4 = 2, 4 % 2 = 0!! нод = 2
    # 51 и 34:  51 % 34 = 17, 34 % 17 = 0!! нод = 17
    # 46 % 18:  46 % 18 = 10, 18 % 10 = 8, 10 % 8 = 2, 8 % 2 = 0!!  нод  = 2
    # a и b :     a % b = a, a % b = a

    # Быстрый алгоритм Евклида = пока меньшее число больше 0, 
    # большему числу присваиваем остаток от деления на меньшее число
    # и после выводим большее число

def nod(a, b):  
    ''' Вычисляем НОД для натуральных чисел a и b
    по быстрому алгоритму Евклида
    : param a: первое натуральное число
    : param b: второе натуральное число
    return: НОД 
    '''    
    if a < b: 
        a,b = b,a # если a < b то соответственно поменяем значение между этими двумя переменными
            # 46 % 18:  46 % 18 = 10, 18 % 10 = 8, 10 % 8 = 2, 8 % 2 = 0!!  нод  = 2
    while b != 0:
        element = b
        menshee_znachenie_soxranaem_v_b = a % b
        print(f'{a} % {b} = {menshee_znachenie_soxranaem_v_b} ')
      
        a, b = b, a % b   # и возвращаться будет наибольшее а
                          # левая сторона b, a % b --- когда мы делаем операцию a % b оно будет заведомо меньше чем b,
                          # поэтому большее значение всегда будет сохраняться в переменной а из a, b (правая сторона)
                          # а меньшее всегда в переменной b из a, b (правая сторона) выражения a, b = b, a % b 
                          # и когда b == 0, мы возвращаем return a, большее значение а, НОД  
    print(f'НОД: {element}')   
    return a    
# func = nod(a, b)
# print(f'для теста нод', func)

def nok(a, b):   
    nokk = (a * b) // (nod(a, b)) # // делится без остатка, с одной чертой будет 166.0
    print(f'НОК: {nokk}')
    return nokk
nok(a, b)
print("")



def res(a,b):
    m = a * b
    while a != 0 and b != 0:
        
        if a > b:
            if a <= 0 : break
            else:
                menshee_znachenie_soxranaem = a % b
                print(f'{a} % {b} = {menshee_znachenie_soxranaem} ')
            
            element = b
            a %= b
        else: 
            if b <= 0 : break
            else:
                menshee_znachenie_soxranaem2 = b % a
                print(f'{b} % {a} = {menshee_znachenie_soxranaem2} ')  
            element = a  
            b %= a
    print(f'НОД: {element}') 
    res = m // (a+b)  
    print(f'НОК: {res}') 
    return res


def vvod_2_number():      # функция которая передает изнутри данные ()       
    while True:
        try: 
            a, b, *c = list(map(int , input(f'Введите 2  числа\n').split())) 
            # *c - является мусорной переменной и берет на себя любые цифры которые введут лишние
            print(f'Вводим данные: {a, b}') 
            return a, b
        except ValueError:
            print("Вы ввели не число. Повторите ввод")
       
a,b = vvod_2_number()            
res(a,b) 


# try: 
# except: print("ошибка ввода")

# print(f'Вводим данные: {a, b}')
# if (a <= 0) or (b <= 0):
#     print("данные некорректны, ничего не гарантирую")
# try:
#     if (a <= 0) and (b <= 0): 
#         print("данные некорректны, ничего не гарантирую")
# except: print("ошибка ввода")




# '''тесты '''
# def test_nod(func):
#     # 1  тест 
#     a = 28
#     b = 35
#     res = nod(a, b)
#     if res == 7:
#         print('#test1 - ок')
#     else: print('#test1 - fail')

#     # 2  тест вычисляет наибольшой общий делитель нод
#     a = 100
#     b = 1
#     res = func(a, b)
#     if res == 1:
#         print('#test1 - ок')
#     else: print('#test1 - fail')

#     # 3  тест - определяет скорость работы данной функции 
#     a = 2
#     b = 1000000000000000000000
#     st = time.time()
#     res = func(a, b)
#     et = time.time() 
#     dt = et - st
#     if res == 2 and dt < 1:
#         print('#test1 - ок')
#     else: print('#test1 - fail')

# test_nod(nod)
# print("")








# import random


# a = random.randint(-10,90)
# if a == 0:
#     a = random.randint(1,90) # если попали рандом то заново рандом пускаем, но уже без 0
# b = random.randint(-10,90)
# print(f'Вводим данные: {a, b}')

# if (a <= 0) or (b <= 0):
#     print("данные некорректны, ничего не гарантирую")  # проверяем корректность введенных данных
# def nod(a, b):              # 60 % 48 = 12
#         if a < b: temp = a
#         else: temp = b

#         for i in range(1, temp + 1): 
#             if(( a % i == 0) and(b % i == 0 )): 
#                 gcd = i 
#                 print(gcd)
                  
#             return gcd
#         else: gcd

# def nok(a, b):   
#     nokk = (a * b) // (nod(a, b)) # // делится без остатка, с одной чертой будет 166.0
#     print(f'НОК: {nokk}')
#     return nokk
# nok(a, b)















# # A = int(input("A="))
# # B = int(input("B="))
# A = 25 
# B = 5

# def gcd(a, b):
#     if(a < b):
#         (a, b) = (b, a)
#     return gcd(b, a % b) if b != 0 else a


# def lcm(a, b):
#     return a / gcd(a, b) * b


# print(lcm(A, B))


# вводим начальные данные
# a = int (input("Введите первое число: "))
# b = int (input("Введите второе число: "))
# a = 12
# b = 2


# # проверяем корректность введенных данных
# if (a <= 0) or (b <= 0): print("данные некорректны, ничего не гарантирую")

# # определяем НОД чисел a и b
# x, y = a, b
# while (y > 0): x, y = y, x%y
# print("НОД равен", x) # маленький бонус

# # вычисляем НОК
# c = a * b / x

# # выводим ответ
# print("НОК равен", c)


def max_common_divisor(a, b):
    temp = 0
    while b != 0:
        temp = b
        b = a % b
        a = temp
    print(a)
    return a
def min_common_divisor(a, b):
    return (a * b) / max_common_divisor(a, b)

noks = min_common_divisor(a, b)
print(f"Наименьшее общее кратное {a} и {b} равно {noks}.")
