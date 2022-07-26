# 41. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
    
#     *Пример:* 
    
#     2+2 => 4; 
    
#     1+2*3 => 7; 
    
#     1-2*3 => -5;
    
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
        
#         *Пример:* 
        
#         1+2*3 => 7; 
        
#         (1+2)*3 => 9;


import random

def rand_operas():
    n1 = random.randint(0,20)
    n2 = random.randint(0,20)
    # operas = input(f'Введите операцию (+, -, /, *, mod, pow, div)')

    allText = '+ - / * mod pow div'
    lir = list ( map ( str , allText.split()))
    operas = random.choice(lir)
    print(n1, operas, n2)
    return n1, operas, n2



def calk(n1, operas, n2): 
    n1 = int(n1) # переводим в целочисленные значения
    n2 = int(n2)

    if operas == '%': operas = 'mod' # по заданию у нас должны быть такие выражения ниже, переводим
    elif operas == '**': operas = 'pow'
    elif operas == '//': operas = 'div'

    if operas == '+': print(n1 + n2)
    elif operas == '-': print(n1 - n2)
    elif operas == '*': print(n1 * n2)
    elif operas == '/': 
        if n2 == 0: print("Деление на 0!")
        else: print(n1 / n2)
    elif operas == 'mod': print(n1 % n2)
    elif operas == 'pow': print(n1 ** n2)
    elif operas == 'div': print(n1 // n2)
    # else: print('Неверная операция')
    return operas
n1, operas, n2 = rand_operas()
calk(n1, operas, n2)

