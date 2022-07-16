# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

import random
import string
def generate_alphanum_random_string(length): # генерируем рандомную строку из чисел и букв
    length = random.randint(1,12)
    for i in range(length):
        letters_and_digits = string.ascii_letters + string.digits
        rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string 
def generate_stroki(stroka): # генерируем много строк из чисел и букв
    mnogo_trok = []
    for i in generate_alphanum_random_string(stroka):
        mnogo_trok.append(generate_alphanum_random_string(stroka))
    return mnogo_trok
def numder(my_list): # ищем в строках любые числа и выводим на экран
    count = 0
    col = 0
    num = []
    for i in my_list:
        for x in str(i):    
            if x  >= str('0') and x <= str('9') :
                count = 1
                col += 1
                num += str(x)     
    if count == 1: print(f'В заданном списке присутствует {col} {adapter_clova_chislo(col)} {num}')
    else:print('нет чисел')
    return my_list
def adapter_clova_chislo(number): # окончание исправляем у слова число в выводе
    a = number % 10 # a - остаток от деления, number - число
    if number > 0: 
        if (11 <= number <= 12): return 'чисел' 
        elif (a == 0): return 'чисел' 
        elif (a == 1): return 'число'
        elif 2 <= a <= 4: return 'числа'
        elif 5 <= a <= 9: return 'чисел'
my_list = []
Lists = (generate_alphanum_random_string(my_list))
List2 = generate_stroki(Lists)
print(List2)    
numder(List2)
 


