# На вход подается строка
# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: 
# первое число, второе число и операцию, после чего применяет операцию к введённым числам 
# ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.
# 5*8

''' немного отступил от темы, если нужно заполнить 2 строки сразу'''
# lst1 = []
# lst2 = []
# for i in range(2):
#     a, b = map(int, input().split())
#     lst1.append(a)
#     lst2.append(b)
 
# print(f'lst 1: {lst1}')
# print(f'lst 2: {lst2}')

# 1 ариант
# def Calc(arg_one, arg_two, operation):
#     if operation == '+':
#         return arg_one + arg_two
#     if operation == '-':
#         return arg_one - arg_two
#     if operation == '*':
#         return arg_one * arg_two
#     if operation == '/':
#         if arg_two == 0:
#             return "Деление на 0!"
#         return arg_one / arg_two
#     if operation == '%':
#         return arg_one % arg_two
#     if operation == '//':
#         return arg_one // arg_two
#     if operation == '**':
#         return arg_one ** arg_two


# status = True
# while status != False:
#     arg_one, operation, arg_two = map(str, input().split())
#     arg_one = float(arg_one)
#     arg_two = float(arg_two)
#     result = Calc(arg_one, arg_two, operation)
#     print(result)

#     status = input('Введите "q", чтобы выйти из программы.')
#     if status == 'q' or status == 'quit':
#         status = False
# break

# 2 вариант
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

# n1, operas, n2 = map(str, input().split())
# n1, operas, n2 = (i for i in str(input()).split()) # создаем единую строчку из 3 элементов выражения
# объявлена строка ввода данных input(). Функция .split() разделяет ее на список необходимых нам строк: в данном случае 3

# 2 % 4 = 2 это уже остаток отделения 2

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



# #дешифратор
# alphabet_list = str(input("Введите пример: "))
# str_a=''
# str_b=''
# t=0
# C = ''
# for i in alphabet_list: 
#      if chr(ord(i))=='+' or chr(ord(i))=='-' or chr(ord(i))=='*' or chr(ord(i))=='/':
#       C = chr(ord(i))
#       t=1
#      elif t==0:
#         str_a = str_a+''.join(chr(ord(i)))
#      elif t==1:
#         str_b = str_b+''.join(chr(ord(i)))    
# A = float(str_a)
# B = float(str_b)

# #тело калькулятора
# if C == '/':
#     if B==0:
#         print ('На ноль делить нельзя')
#     else:
#          print (A/B)
# if C == '+': 
#     print (A+B)
# if C == '-': 
#     print (A-B)
# if C == '*': 
#     print (A*B)






# def calk(a,b,action):
#     if action == '+':
#         print(a + b)
#     elif action == '-':
#         print(a - b)
#     elif action == '*':
#         print(a * b)
#     elif action == '/':
#         if  b == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(a / b)
#     elif action == 'mod':
#         print(a % b)
#     elif action == 'pow':
#         print(a ** b)
#     elif action == 'dif':
#         print(a // b)
#     else:
#         print('Неверная операция')
#     return action

# a = float(input('Введите число 1\n'))
# b = float(input('Введите число 2\n'))
# action = input('Введиете  операцию (+, -, /, *, mod, pow, div)')
# calk(a,b,action)



    